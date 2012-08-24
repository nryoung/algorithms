"""
Tools for testing
-----------------

nose.tools provides a few convenience functions to make writing tests
easier. You don't have to use them; nothing in the rest of nose depends
on any of these methods.
"""
import re
import time
import unittest


__all__ = ['ok_', 'eq_', 'make_decorator', 'raises', 'set_trace', 'timed',
            'with_setup', 'TimeExpired', 'istest', 'nottest']


class TimeExpired(AssertionError):
    pass


def ok_(expr, msg=None):
    """Shorthand for assert. Saves 3 whole characters!
    """
    assert expr, msg


def eq_(a, b, msg=None):
    """Shorthand for 'assert a == b, "%r != %r" % (a, b)
    """
    assert a == b, msg or "%r != %r" % (a, b)


def make_decorator(func):
    """
    Wraps a test decorator so as to properly replicate metadata
    of the decorated function, including nose's additional stuff
    (namely, setup and teardown).
    """
    def decorate(newfunc):
        if hasattr(func, 'compat_func_name'):
            name = func.compat_func_name
        else:
            name = func.__name__
        newfunc.__dict__ = func.__dict__
        newfunc.__doc__ = func.__doc__
        newfunc.__module__ = func.__module__
        if not hasattr(newfunc, 'compat_co_firstlineno'):
            newfunc.compat_co_firstlineno = func.func_code.co_firstlineno
        try:
            newfunc.__name__ = name
        except TypeError:
            # can't set func name in 2.3
            newfunc.compat_func_name = name
        return newfunc
    return decorate


def raises(*exceptions):
    """Test must raise one of expected exceptions to pass.

    Example use::

      @raises(TypeError, ValueError)
      def test_raises_type_error():
          raise TypeError("This test passes")

      @raises(Exception)
      def test_that_fails_by_passing():
          pass

    If you want to test many assertions about exceptions in a single test,
    you may want to use `assert_raises` instead.
    """
    valid = ' or '.join([e.__name__ for e in exceptions])
    def decorate(func):
        name = func.__name__
        def newfunc(*arg, **kw):
            try:
                func(*arg, **kw)
            except exceptions:
                pass
            except:
                raise
            else:
                message = "%s() did not raise %s" % (name, valid)
                raise AssertionError(message)
        newfunc = make_decorator(func)(newfunc)
        return newfunc
    return decorate


def set_trace():
    """Call pdb.set_trace in the calling frame, first restoring
    sys.stdout to the real output stream. Note that sys.stdout is NOT
    reset to whatever it was before the call once pdb is done!
    """
    import pdb
    import sys
    stdout = sys.stdout
    sys.stdout = sys.__stdout__
    pdb.Pdb().set_trace(sys._getframe().f_back)
    

def timed(limit):
    """Test must finish within specified time limit to pass.

    Example use::

      @timed(.1)
      def test_that_fails():
          time.sleep(.2)
    """
    def decorate(func):
        def newfunc(*arg, **kw):
            start = time.time()
            func(*arg, **kw)
            end = time.time()
            if end - start > limit:
                raise TimeExpired("Time limit (%s) exceeded" % limit)
        newfunc = make_decorator(func)(newfunc)
        return newfunc
    return decorate


def with_setup(setup=None, teardown=None):
    """Decorator to add setup and/or teardown methods to a test function::

      @with_setup(setup, teardown)
      def test_something():
          " ... "

    Note that `with_setup` is useful *only* for test functions, not for test
    methods or inside of TestCase subclasses.
    """
    def decorate(func, setup=setup, teardown=teardown):
        if setup:
            if hasattr(func, 'setup'):
                _old_s = func.setup
                def _s():
                    setup()
                    _old_s()
                func.setup = _s
            else:
                func.setup = setup
        if teardown:
            if hasattr(func, 'teardown'):
                _old_t = func.teardown
                def _t():
                    _old_t()
                    teardown()
                func.teardown = _t
            else:
                func.teardown = teardown
        return func
    return decorate


def istest(func):
    """Decorator to mark a function or method as a test
    """
    func.__test__ = True
    return func


def nottest(func):
    """Decorator to mark a function or method as *not* a test
    """
    func.__test__ = False
    return func

#
# Expose assert* from unittest.TestCase
# - give them pep8 style names
#
caps = re.compile('([A-Z])')

def pep8(name):
    return caps.sub(lambda m: '_' + m.groups()[0].lower(), name)

class Dummy(unittest.TestCase):
    def nop():
        pass
_t = Dummy('nop')

for at in [ at for at in dir(_t)
            if at.startswith('assert') and not '_' in at ]:
    pepd = pep8(at)
    vars()[pepd] = getattr(_t, at)
    __all__.append(pepd)

del Dummy
del _t
del pep8
