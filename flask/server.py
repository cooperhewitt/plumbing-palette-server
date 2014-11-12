#!/usr/bin/env python

import logging

import flask
from flask_cors import cross_origin 
from werkzeug.contrib.fixers import ProxyFix

import roygbiv

try:
    # https://github.com/cooperhewitt/py-cooperhewitt-swatchbook
    import cooperhewitt.swatchbook as swatchbook
except Exception, e:
    import swatchbook

try:
    # https://github.com/cooperhewitt/py-cooperhewitt-flask
    import cooperhewitt.flask.http_pony as http_pony
except Exception, e:
    import http_pony

app = flask.Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():

    return flask.jsonify({'stat': 'ok'})
    
if __name__ == '__main__':

    import sys
    import optparse
    import ConfigParser

    parser = optparse.OptionParser()

    parser.add_option("-c", "--config", dest="config", help="", action="store", default=None)
    parser.add_option("-v", "--verbose", dest="verbose", help="enable chatty logging; default is false", action="store_true", default=False)

    opts, args = parser.parse_args()

    if opts.verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("verbose logging is enabled")
    else:
        logging.basicConfig(level=logging.INFO)

    cfg = ConfigParser.ConfigParser()
    cfg.read(opts.config)

    http_pony.update_app_config(app, cfg)

    port = cfg.get('flask', 'port')
    port = int(port)

    app.run(port=port)
