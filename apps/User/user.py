from flask_login import UserMixin,current_user
from utils.db import db


class User(db.Model, UserMixin):
    __tablename__ = 'stacks_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(100), nullable=False)
    upassword = db.Column(db.String(100), nullable=True)
    #后续要和书对应,登录了用户，才能对应上传的书，否则书的上传者就是匿名
    books = db.relationship('Book', backref='user', lazy=True)

    def is_authenticated(self):
        if self._authenticated:
            return self._authenticated
        current_user = User.query.get(2)
        return True


    def is_anonymous(self):
        current_user = User.query.get(2)
        return True