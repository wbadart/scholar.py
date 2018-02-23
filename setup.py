#!/usr/bin/env python3

'''
setup.py
created: FEB 2018
'''

from setuptools import find_packages, setup


setup(name='scholar',
      version='2.11.0',
      packages=['scholar'],
      py_modules=['scholar'],
      install_requires=[
          'beautifulsoup4',
      ],
      entry_points={
          'console_scripts': [
              'gscholar = scholar:main'
          ],
      },
      zip_safe=False)
