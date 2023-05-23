from flask import Flask
from config import get_flask_config
from utils import db as utils_db
from utils import response as utils_response
from utils.hooks import before_request_hooks, after_request_hooks

def init_bp(app):
    from .Book import bp_book
    app.register_blueprint(bp_book, url_prefix="/book")

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(get_flask_config)

    #初始化数据库
    utils_db.init_db(app)

    #初始化蓝图
    init_bp(app)

    #异常处理
    utils_response.errorhandler(app)

    # 请求钩子
    before_request_hooks(app)
    after_request_hooks(app)

    return app

