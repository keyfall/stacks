from flask import Flask, render_template
from flask_login import current_user
from config import get_flask_config
from utils import db as utils_db
from utils import response as utils_response
from utils.hooks import before_request_hooks, after_request_hooks
from utils.login import login_manager


def init_bp(app):
    from .Book import bp_book
    from .User import bp_user

    app.register_blueprint(bp_book, url_prefix="/book")
    app.register_blueprint(bp_user, url_prefix="/user")

    @app.route('/')
    def index():
        return render_template('index.html',user=current_user)

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(get_flask_config)

    #初始化数据库
    utils_db.db.init_app(app)
    #重载数据库
    utils_db.reload_database(app)
    #初始化蓝图
    init_bp(app)

    #异常处理
    utils_response.errorhandler(app)

    # 请求钩子
    before_request_hooks(app)
    after_request_hooks(app)

    # flask-login用户会话管理
    login_manager.init_app(app)

    return app

