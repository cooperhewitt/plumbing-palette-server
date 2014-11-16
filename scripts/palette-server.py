#!/usr/bin/env python

import os
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

def before_first():

    try:

        if app.config.get('HTTP_PONY_INIT', None):
            return True

        if os.environ.get("PALETTE_SERVER_CONFIG"):
            
            cfg = os.environ.get("PALETTE_SERVER_CONFIG")
            cfg = http_pony.update_app_config_from_file(app, cfg)

            return True

    except Exception, e:

        logging.error("failed to load config file, because %s" % e)
        flask.abort(500)

    logging.error("missing config file")
    flask.abort(500)

app.before_first_request(before_first)

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():

    return flask.jsonify({'stat': 'ok'})

@app.route('/extract/roygbiv/<reference>', methods=['GET', 'POST'])
@cross_origin(methods=['GET'])
def extract_roygbiv(reference):

    try:
        if flask.request.method=='POST':
            path = http_pony.get_upload_path(app)
        else:
            path = http_pony.get_local_path(app)

    except Exception, e:
        logging.error(e)
        flask.abort(400)

    ok = True

    try:
        rsp = _extract(path, reference)
    except Exception, e:
        logging.error("Unable to extract colors, because %s" % e)
        ok = False

    if flask.request.method == 'POST':
        os.unlink(path)

    if not ok:
        flask.abort(500)

    return flask.jsonify(**rsp)

def _extract(path, reference):

    logging.debug("get palette for %s, with %s" % (path, reference))

    ref = swatchbook.load_palette(reference)

    roy = roygbiv.Roygbiv(path)
    average = roy.get_average_hex()
    palette = roy.get_palette_hex()

    def prep(hex):
        c_hex, c_name = ref.closest(hex)        
        return {'color': hex, 'closest': c_hex}

    average = prep(average)
    palette = map(prep, palette)
        
    return {
        'reference-closest': reference,
        'average': average,
        'palette': palette
    }

    
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

    cfg = http_pony.update_app_config_from_file(app, opts.config)

    port = cfg.get('flask', 'port')
    port = int(port)

    app.run(port=port)
