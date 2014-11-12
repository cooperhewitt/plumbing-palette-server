#!/usr/bin/env python

# THIS DOES NOT WORK YET

from distutils.core import setup

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
      install_requires = [
          'https://github.com/cooperhewitt/py-cooperhewitt-flask/archive/v0.1.tar.gz',
          'https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/archive/v0.2.tar.gz',
      ],
      packages=[],
      scripts=[],
      download_url='',
      license='BSD')
