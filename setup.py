import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='algorithms',
      version='1.0',
      description='module of algorithms for Python',
      long_description=long_description(),
      url='https://github.com/nryoung/algorithms',
      author='Nic Young',
      author_email='nryoung@gmail.com',
      license='BSD',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          ],
      zip_safe=False)
