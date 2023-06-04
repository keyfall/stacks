from utils.db import db


class Book(db.Model):
    __tablename__ = 'stacks_book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(100), nullable=False)
    book_url = db.Column(db.String(200), nullable=False)
    #后续要和作者对应,登录了用户，才能对应上传的书，否则书的上传者就是匿名