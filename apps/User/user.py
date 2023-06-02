from utils.db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'stacks_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(100), nullable=False)
    upassword = db.Column(db.String(100), nullable=False)
    #后续要和书对应,登录了用户，才能对应上传的书，否则书的上传者就是匿名