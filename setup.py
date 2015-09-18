from setuptools import setup

#Read in the README for the long description on PyPI
def long_description():
    with open('README.rst', 'r') as f:
        readme = unicode(f.read())
    return readme

setup(name='algorithms',
      version='0.1',
      description='module of algorithms for Python',
      long_description=long_description(),
      url='https://github.com/nryoung/algorithms',
      author='Nic Young',
      author_email='nryoung@gmail.com',
      license='BSD',
      packages=['algorithms', 'algorithms.data_structure', 'algorithms.dynamic_programming', 'algorithms.sorting', 'algorithms.shuffling',
          'algorithms.searching', 'algorithms.math', 'algorithms.tests'],
      classifiers=[
          'Programming Language :: Python :: 2.7',],
      zip_safe=False)
