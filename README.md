# plumbing-palette-server

A simple HTTP pony server for doing colour extraction. THIS IS NOT READY FOR USE YET.

## Setup

	python ./flask/server.py -c server.cfg
	INFO:werkzeug: * Running on http://127.0.0.1:5000/

## Endpoints

### GET /ping 

	curl -X GET 'http://localhost:5000/ping'

	{
		"stat": "ok"
	}

### GET /extract/roygbiv/<REFERENCE>

	curl -X GET 'http://localhost:5000/extract/roygbiv/css3?file=test.jpg'

	{
	  "average": {
	    "closest": "#808080", 
	    "color": "#8d7d73"
	  }, 
	  "palette": [
	    {
	      "closest": "#e9967a", 
	      "color": "#d99e82"
	    }, 
	    {
	      "closest": "#d3d3d3", 
	      "color": "#ddd4c9"
	    }, 
	    {
	      "closest": "#800000", 
	      "color": "#4d2415"
	    }, 
	    {
	      "closest": "#cd5c5c", 
	      "color": "#a96a4f"
	    }, 
	    {
	      "closest": "#2f4f4f", 
	      "color": "#343136"
	    }
	  ], 
	  "reference-closest": "css3"
	}

### POST /extract/roygbiv/<REFERENCE>

## Config

`plumbing-palette-server` uses utility functions exported by the
[cooperhewitt.flask.http_pony](https://github.com/cooperhewitt/py-cooperhewitt-flask/blob/master/cooperhewitt/flask/http_pony.py)
library which checks your Flask application's configuration for details about
how to handle things.

The following settings should be added to a standard [ini style configutation
file](https://en.wikipedia.org/wiki/INI_file).

### [flask]

#### port

The Unix TCP port you want your Flask server to listen on.

### [http_pony]

#### local_path_root

If set then files sent using an `HTTP GET` parameter will be limited to only
those that are are parented by this directory.

If it is not set then `HTTP GET` requests will fail.

#### upload_path_root

If set then files sent as an `HTTP POST` request will be first written to this
directory before processing.

If not set then the operating system's temporary directory will be used.

#### allowed_extensions

A comma-separate list of valid file extensions for processing.

## Dependencies

### Things you'll need to install yourself

_Pending a proper `setup.py` file._

* [Flask](http://flask.pocoo.org/)
* [Flask-Cors](https://pypi.python.org/pypi/Flask-Cors/)

### Things that come pre-bundled

_The following are required but are available as libraries local to the server itself if not already pre-installed._

* [cooperhewitt.flask.http_pony](https://github.com/cooperhewitt/py-cooperhewitt-flask)
* [cooperhewitt.swatchbook](https://github.com/cooperhewitt/py-cooperhewitt-swatchbook)
* [RoyGBiv](https://pypi.python.org/pypi/RoyGBiv/)

## To do:

* A proper `setup.py` file

