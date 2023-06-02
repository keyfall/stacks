from flask_login import LoginManager
from apps.User.user import User

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message_category = "info"
login_manager.login_message = "Access denied"


@login_manager.user_loader
def load_user(user_id):
    # 需要先进行数据库检查
    return User.query.get(int(user_id))


@login_manager.request_loader
def request_loader(request):
    uname = request.form.get("uname")

    return User.query.filter_by(uname=uname).first()
