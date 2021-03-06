"""
setup for the pylatexc package
a package for embedding python code in latex documents
"""

from setuptools import setup, find_packages

__version__ = '0.1.0'
__author__ = 'Michael Belousov'

setup(name='pylatexc',
      version=__version__,
      author=__author__,
      description='A compiler of pylatex files into normal tex files',
      url='',
      packages=find_packages(),
      install_requires=[ 'six' ])
