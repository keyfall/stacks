import json

from flask_login import LoginManager
from apps.User.user import User




login_manager = LoginManager()
login_manager.login_view = "/user/login"
login_manager.login_message_category = "info"
login_manager.login_message = "Access denied"

# 创建一个匿名用户类


@login_manager.user_loader
def load_user(user_id):

    # 需要先进行数据库检查
    # if user_id == None:
    #     return User.query.get(2)
    return User.query.get(int(user_id)) or User.query.get(2)


@login_manager.unauthorized_handler
def unauthorized_callback():
    # 未经授权用户访问需要授权的路由时
    # 直接走佚名用户
    print("进入了unauth")
    return load_user(2)

@login_manager.request_loader
def request_loader(request):

    uname = request.values.get('uname')

    if not uname:
        uname = "佚名"

    user = User.query.filter_by(uname=uname).first()
    print(user)
    if not user:
        return 'Bad login'
    return user

