#!/usr/bin/env python

# THIS DOES NOT WORK YET

from setuptools import setup

setup(name='plumbing-palette-server',
      version='0.1',
      description='',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/plumbing-palette-server',
      requires=[
          'flask',
          # 'flask-cors',
          'roygbiv',
      ],
      dependency_links=[
          'https://github.com/cooperhewitt/py-cooperhewitt-flask/tarball/master#egg=cooperhewitt.flask-0.1',
          'https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/tarball/master#egg=cooperhewitt.swatchbook-0.2',
      ],
      install_requires=[
          'cooperhewitt.flask>=0.1',
          'cooperhewitt.swatchbook>=0.1',
      ],
      packages=[],
      scripts=[
          'scripts/palette-server.py',
      ],
      download_url='',
      license='BSD')
