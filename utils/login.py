from flask_login import LoginManager
from apps.User.user import User
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message_category = "info"
login_manager.login_message = "Access denied"
@login_manager.user_loader
def load_user(uname):
    #需要先进行数据库检查

    user = User()
    user.uname = uname
    return user

@login_manager.request_loader
def request_loader(request):
    user = request.form.get("user")

    user = User()
    user.uname = user
    return user