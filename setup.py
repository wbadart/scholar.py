#!/usr/bin/env python3

'''
setup.py
created: FEB 2018
'''

from setuptools import find_packages, setup


setup(name='scholar.py',
      author='ckreibich',
      version='2.11.0',
      install_requires=[
          'beautifulsoup4',
      ],
      zip_safe=False)
