#!/usr/bin/env python

from setuptools import setup

setup(name='plumbing-palette-server',
      version='0.2',
      description='A Flask based HTTP pony for extracting colours from images',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/plumbing-palette-server',
      requires=[
      ],
      dependency_links=[
          'https://github.com/cooperhewitt/py-cooperhewitt-flask/tarball/master#egg=cooperhewitt.flask-0.34',
          'https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/tarball/master#egg=cooperhewitt.swatchbook-0.3',
      ],
      install_requires=[
          'cooperhewitt.flask',
          'cooperhewitt.swatchbook',
      ],
      packages=[],
      scripts=[
          'scripts/palette-server.py',
      ],
      download_url='https://github.com/cooperhewitt/plumbing-palette-server/tarball/master#egg=0.2',
      license='BSD')
