#!/usr/bin/env python

import os
import logging

import flask
from flask_cors import cross_origin 

import roygbiv

import cooperhewitt.swatchbook as swatchbook
import cooperhewitt.flask.http_pony as http_pony

app = http_pony.setup_flask_app('PALETTE_SERVER')

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

    http_pony.run_from_cli(app)
