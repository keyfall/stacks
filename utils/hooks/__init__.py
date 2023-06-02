from flask import request, jsonify, g

from config import get_white_list
# from utils.log import logger
from utils.response import jsonify_response
from utils.enums import APICODE
from manage import db

white_ip_list = [] if get_white_list.get("ip") == None else get_white_list["ip"].split(",")
white_path_list = [] if get_white_list.get("path") == None else get_white_list["path"].split(",")


def before_request_hooks(app):

    @app.before_request
    def white_list():
        ip = request.remote_addr
        path = request.path

        if ip not in white_ip_list or '/'+path.split('/')[1] not in white_path_list:
            return jsonify_response(code=APICODE.FORBIDDEN, msg="禁止访问")

        engine = db.get_engine()
        g.conn = engine.connect()
        print("starting connection")


def after_request_hooks(app):

    @app.after_request
    def after_app_request(response):
        response_data = response.get_json()
        if g.conn is not None:
            g.conn.close()
            print("closing connection")
        return response