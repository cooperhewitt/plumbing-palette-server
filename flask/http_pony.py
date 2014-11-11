import os.path
import base64
import tempfile
import logging

import flask
import werkzeug
import werkzeug.security

def update_app_config(app, cfg):

    update = {}

    for k, v in cfg.items('http_pony'):

        k = "HTTP_PONY_%s" % k.upper()
        update[k] = v

    app.config.update(**update)

def get_local_path(app, key='file'):

    path = flask.request.args.get(key)
    logging.debug("request path is %s" % path)

    if not path:
        raise Exception, "there's nothing to process"

    root = app.config.get('HTTP_PONY_LOCAL_PATH_ROOT', None)
    logging.debug("image root is %s" % root)

    if not root:
        raise Exception, "image root is not defined"


    if root:

        safe = werkzeug.security.safe_join(root, path)

        if not safe:
            raise Exception, "'%s' + '%s' considered harmful" % (root, path)

        path = safe

    logging.debug("final request path is %s" % path)
    
    if not os.path.exists(path):
        raise Exception, "%s does not exist" % path

    return path

def get_upload_path(app, key='file'):

    file = flask.request.files[key]

    if file and allowed_file(app, file.filename):

        root = app.config.get('HTTP_PONY_UPLOAD_PATH_ROOT', None)

        if not root:
            root = tempfile.gettempdir()

        rand = base64.urlsafe_b64encode(os.urandom(12))
        secure = werkzeug.secure_filename(file.filename)
        fname = "http-pony-%s-%s" % (rand, secure)

        safe = werkzeug.security.safe_join(root, fname)

        if not safe:
            e = "'%s' + '%s' considered harmful" % (root, fname)
            raise Exception, e

        logging.debug("save upload to %s" % safe)

        file.save(safe)
        return safe

    raise Exception, "Missing or invalid file"

def allowed_file(app, filename):

    allowed = app.config.get('HTTP_PONY_ALLOWED_EXTENSIONS', '')
    allowed = allowed.split(',')

    return '.' in filename and filename.rsplit('.', 1)[1] in allowed
