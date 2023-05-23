import json
from flask import jsonify
from datetime import datetime
from utils.enums import APICODE


def jsonify_data(data):
    ret = data
    if isinstance(data, dict):
        ret = {}
        for key, value in data.items():
            ret[jsonify_data(key)] = jsonify_data(value)
    elif isinstance(data, (list, tuple)):
        ret = []
        for value in data:
            ret.append(jsonify_data(value))
    elif isinstance(data, datetime):
        ret = data.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(data, (int, float, str, bool)):
        pass
    else:
        try:
            ret = json.dumps(data)
        except TypeError:
            ret = str(data)
    return ret


def jsonify_response(data='', code=APICODE.OK, msg='ok', **kwargs):
    return jsonify(jsonify_data(dict(
        code=code,
        msg=msg,
        data=data,
        **kwargs
    )))
def errorhandler(app):

    @app.errorhandler(500)
    def handler_500(error):
        return jsonify_response(data=APICODE.ERROR, msg=error if app.conf["ENV"] == "development" else 500)

    @app.errorhandler(400)
    def handler_400(error):
        return jsonify_response(code=APICODE.PARAM_ERROR, msg=error)


