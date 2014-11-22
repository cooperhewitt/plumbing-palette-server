#!/usr/bin/env python

from setuptools import setup

setup(name='plumbing-palette-server',
      version='0.21',
      description='A Flask-based HTTP pony for extracting colors from images',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/plumbing-palette-server',
      requires=[
      ],
      dependency_links=[
          'https://github.com/cooperhewitt/py-cooperhewitt-flask/tarball/master#egg=cooperhewitt.flask-0.34',
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-colors/tarball/master#egg=cooperhewitt.roboteyes-colors-0.1',
      ],
      install_requires=[
          'cooperhewitt.flask',
          'cooperhewitt.roboteyes.colors',
      ],
      packages=[],
      scripts=[
          'scripts/palette-server.py',
      ],
      download_url='https://github.com/cooperhewitt/plumbing-palette-server/tarball/master#egg=0.21',
      license='BSD')
