#!/usr/bin/env python

# THIS DOES NOT WORK YET

from distutils.core import setup

setup(name='plumbing-palette-server',
      version='0.1',
      description='',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/py-cooperhewitt-swatchbook',
      requires=[
          'flask',
          # 'flask-cors',
          'roygbiv',
          'cooperhewitt.flask',
          'cooperhewitt.swatchbook'
      ],
      packages=[],
      scripts=[],
      dependency_links = [
          'https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/releases',
          'https://github.com/cooperhewitt/py-cooperhewitt-flask/releases',
      ],
      download_url='',
      license='BSD')
