"""If you have Ned Batchelder's coverage_ module installed, you may activate a
coverage report with the ``--with-coverage`` switch or NOSE_WITH_COVERAGE
environment variable. The coverage report will cover any python source module
imported after the start of the test run, excluding modules that match
testMatch. If you want to include those modules too, use the ``--cover-tests``
switch, or set the NOSE_COVER_TESTS environment variable to a true value. To
restrict the coverage report to modules from a particular package or packages,
use the ``--cover-packages`` switch or the NOSE_COVER_PACKAGES environment
variable.

.. _coverage: http://www.nedbatchelder.com/code/modules/coverage.html
"""
import logging
import os
import re
import sys
from nose.plugins.base import Plugin
from nose.util import src, tolist

log =  logging.getLogger(__name__)

COVERAGE_TEMPLATE = '''<html>
<head>
%(title)s
</head>
<body>
%(header)s
<style>
.coverage pre {float: left; margin: 0px 1em; border: none;
               padding: 0px; }
.num pre { margin: 0px }
.nocov, .nocov pre {background-color: #faa}
.cov, .cov pre {background-color: #cfc}
div.coverage div { clear: both; height: 1.1em}
</style>
<div class="stats">
%(stats)s
</div>
<div class="coverage">
%(body)s
</div>
</body>
</html>
'''

COVERAGE_STATS_TEMPLATE = '''Covered: %(covered)s lines<br/>
Missed: %(missed)s lines<br/>
Skipped %(skipped)s lines<br/>
Percent: %(percent)s %%<br/>
'''


class Coverage(Plugin):
    """
    Activate a coverage report using Ned Batchelder's coverage module.
    """
    coverTests = False
    coverPackages = None
    _coverInstance = None
    score = 200
    status = {}

    def coverInstance(self):
        if not self._coverInstance:
            import coverage
            try:
                self._coverInstance = coverage.coverage()
            except coverage.CoverageException:
                self._coverInstance = coverage
        return self._coverInstance
    coverInstance = property(coverInstance)

    def options(self, parser, env):
        """
        Add options to command line.
        """
        Plugin.options(self, parser, env)
        parser.add_option("--cover-package", action="append",
                          default=env.get('NOSE_COVER_PACKAGE'),
                          metavar="PACKAGE",
                          dest="cover_packages",
                          help="Restrict coverage output to selected packages "
                          "[NOSE_COVER_PACKAGE]")
        parser.add_option("--cover-erase", action="store_true",
                          default=env.get('NOSE_COVER_ERASE'),
                          dest="cover_erase",
                          help="Erase previously collected coverage "
                          "statistics before run")
        parser.add_option("--cover-tests", action="store_true",
                          dest="cover_tests",
                          default=env.get('NOSE_COVER_TESTS'),
                          help="Include test modules in coverage report "
                          "[NOSE_COVER_TESTS]")
        parser.add_option("--cover-inclusive", action="store_true",
                          dest="cover_inclusive",
                          default=env.get('NOSE_COVER_INCLUSIVE'),
                          help="Include all python files under working "
                          "directory in coverage report.  Useful for "
                          "discovering holes in test coverage if not all "
                          "files are imported by the test suite. "
                          "[NOSE_COVER_INCLUSIVE]")
        parser.add_option("--cover-html", action="store_true",
                          default=env.get('NOSE_COVER_HTML'),
                          dest='cover_html',
                          help="Produce HTML coverage information")
        parser.add_option('--cover-html-dir', action='store',
                          default=env.get('NOSE_COVER_HTML_DIR', 'cover'),
                          dest='cover_html_dir',
                          metavar='DIR',
                          help='Produce HTML coverage information in dir')

    def configure(self, options, config):
        """
        Configure plugin.
        """
        try:
            self.status.pop('active')
        except KeyError:
            pass
        Plugin.configure(self, options, config)
        if config.worker:
            return
        if self.enabled:
            try:
                import coverage
            except ImportError:
                log.error("Coverage not available: "
                          "unable to import coverage module")
                self.enabled = False
                return
        self.conf = config
        self.coverErase = options.cover_erase
        self.coverTests = options.cover_tests
        self.coverPackages = []
        if options.cover_packages:
            for pkgs in [tolist(x) for x in options.cover_packages]:
                self.coverPackages.extend(pkgs)
        self.coverInclusive = options.cover_inclusive
        if self.coverPackages:
            log.info("Coverage report will include only packages: %s",
                     self.coverPackages)
        self.coverHtmlDir = None
        if options.cover_html:
            self.coverHtmlDir = options.cover_html_dir
            log.debug('Will put HTML coverage report in %s', self.coverHtmlDir)
        if self.enabled:
            self.status['active'] = True

    def begin(self):
        """
        Begin recording coverage information.
        """
        log.debug("Coverage begin")
        self.skipModules = sys.modules.keys()[:]
        if self.coverErase:
            log.debug("Clearing previously collected coverage statistics")
            self.coverInstance.erase()
        self.coverInstance.exclude('#pragma[: ]+[nN][oO] [cC][oO][vV][eE][rR]')
        self.coverInstance.start()

    def report(self, stream):
        """
        Output code coverage report.
        """
        log.debug("Coverage report")
        self.coverInstance.stop()
        self.coverInstance.save()
        modules = [ module
                    for name, module in sys.modules.items()
                    if self.wantModuleCoverage(name, module) ]
        log.debug("Coverage report will cover modules: %s", modules)
        self.coverInstance.report(modules, file=stream)
        if self.coverHtmlDir:
            log.debug("Generating HTML coverage report")
            if hasattr(self.coverInstance, 'html_report'):
                self.coverInstance.html_report(modules, self.coverHtmlDir)
            else:
                self.report_html(modules)

    def report_html(self, modules):
        if not os.path.exists(self.coverHtmlDir):
            os.makedirs(self.coverHtmlDir)
        files = {}
        for m in modules:
            if hasattr(m, '__name__') and hasattr(m, '__file__'):
                files[m.__name__] = m.__file__
        self.coverInstance.annotate(files.values())
        global_stats =  {'covered': 0, 'missed': 0, 'skipped': 0}
        file_list = []
        for m, f in files.iteritems():
            if f.endswith('pyc'):
                f = f[:-1]
            coverfile = f+',cover'
            outfile, stats = self.htmlAnnotate(m, f, coverfile,
                                               self.coverHtmlDir)
            for field in ('covered', 'missed', 'skipped'):
                global_stats[field] += stats[field]
            file_list.append((stats['percent'], m, outfile, stats))
            os.unlink(coverfile)
        file_list.sort()
        global_stats['percent'] = self.computePercent(
            global_stats['covered'], global_stats['missed'])
        # Now write out an index file for the coverage HTML
        index = open(os.path.join(self.coverHtmlDir, 'index.html'), 'w')
        index.write('<html><head><title>Coverage Index</title></head>'
                    '<body><p>')
        index.write(COVERAGE_STATS_TEMPLATE % global_stats)
        index.write('<table><tr><td>File</td><td>Covered</td><td>Missed'
                    '</td><td>Skipped</td><td>Percent</td></tr>')
        for junk, name, outfile, stats in file_list:
            stats['a'] = '<a href="%s">%s</a>' % (outfile, name)
            index.write('<tr><td>%(a)s</td><td>%(covered)s</td><td>'
                        '%(missed)s</td><td>%(skipped)s</td><td>'
                        '%(percent)s %%</td></tr>' % stats)
        index.write('</table></p></html')
        index.close()

    def htmlAnnotate(self, name, file, coverfile, outputDir):
        log.debug('Name: %s file: %s' % (name, file, ))
        rows = []
        data = open(coverfile, 'r').read().split('\n')
        padding = len(str(len(data)))
        stats = {'covered': 0, 'missed': 0, 'skipped': 0}
        for lineno, line in enumerate(data):
            lineno += 1
            if line:
                status = line[0]
                line = line[2:]
            else:
                status = ''
                line = ''
            lineno = (' ' * (padding - len(str(lineno)))) + str(lineno)
            for old, new in (('&', '&amp;'), ('<', '&lt;'), ('>', '&gt;'),
                             ('"', '&quot;'), ):
                line = line.replace(old, new)
            if status == '!':
                rows.append('<div class="nocov"><span class="num"><pre>'
                            '%s</pre></span><pre>%s</pre></div>' % (lineno,
                                                                    line))
                stats['missed'] += 1
            elif status == '>':
                rows.append('<div class="cov"><span class="num"><pre>%s</pre>'
                            '</span><pre>%s</pre></div>' % (lineno, line))
                stats['covered'] += 1
            else:
                rows.append('<div class="skip"><span class="num"><pre>%s</pre>'
                            '</span><pre>%s</pre></div>' % (lineno, line))
                stats['skipped'] += 1
        stats['percent'] = self.computePercent(stats['covered'],
                                               stats['missed'])
        html = COVERAGE_TEMPLATE % {'title': '<title>%s</title>' % name,
                                    'header': name,
                                    'body': '\n'.join(rows),
                                    'stats': COVERAGE_STATS_TEMPLATE % stats,
                                   }
        outfilename = name + '.html'
        outfile = open(os.path.join(outputDir, outfilename), 'w')
        outfile.write(html)
        outfile.close()
        return outfilename, stats

    def computePercent(self, covered, missed):
        if covered + missed == 0:
            percent = 1
        else:
            percent = covered/(covered+missed+0.0)
        return int(percent * 100)

    def wantModuleCoverage(self, name, module):
        if not hasattr(module, '__file__'):
            log.debug("no coverage of %s: no __file__", name)
            return False
        module_file = src(module.__file__)
        if not module_file or not module_file.endswith('.py'):
            log.debug("no coverage of %s: not a python file", name)
            return False
        if self.coverPackages:
            for package in self.coverPackages:
                if (re.findall(r'^%s\b' % re.escape(package), name)
                    and (self.coverTests
                         or not self.conf.testMatch.search(name))):
                    log.debug("coverage for %s", name)
                    return True
        if name in self.skipModules:
            log.debug("no coverage for %s: loaded before coverage start",
                      name)
            return False
        if self.conf.testMatch.search(name) and not self.coverTests:
            log.debug("no coverage for %s: is a test", name)
            return False
        # accept any package that passed the previous tests, unless
        # coverPackages is on -- in that case, if we wanted this
        # module, we would have already returned True
        return not self.coverPackages

    def wantFile(self, file, package=None):
        """If inclusive coverage enabled, return true for all source files
        in wanted packages.
        """
        if self.coverInclusive:
            if file.endswith(".py"):
                if package and self.coverPackages:
                    for want in self.coverPackages:
                        if package.startswith(want):
                            return True
                else:
                    return True
        return None
