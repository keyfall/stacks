from apps.User import bp_user
from flask import render_template, request, redirect
from flask_login import login_user

from utils.login_utils import require_names
from .user import User
from apps.Book.book import Book
from utils.db import db
from flask_login import login_required


@bp_user.route('/verify_book', methods=["GET", "POST"])
@login_required
@require_names('keyfall')
def login():
    if request.method == 'GET':
        return '''
                   <form action='/user/verify_book' method='POST'>
                    <input type='text' name='uname' placeholder='uname'/>
                    <input type='password' name='password' id='password' placeholder='password'/>
                    <input type='submit' name='submit'/>
                   </form>
                   '''

    uname =  request.form['uname']
    password =  request.form['password']
    user_result = User.query.filter_by(uname=uname, upassword=password).first()
    if not user_result:
        return '''
                    Bad login&nbsp;&nbsp;&nbsp;<a href='/user/login'>返回</a>
                '''

    user = user_result
    login_user(user, remember=True)

    pagination = Book.query.filter_by(verify='0', logic_delete='0').order_by(Book.create_time.desc()).paginate(page=1,per_page=10,error_out=False)
    books = pagination.items
    context = {
        "books":books,
        "uname":uname,
        "pagination": pagination
    }

    return render_template("audit.html", **context)

@bp_user.route('/create_user', methods=["GET", "POST"])
def create():
    users = [
    User(uname="keyfall", upassword="zongming"),
    User(uname="佚名", upassword=""),
        ]
    db.session.add_all(users)
    db.session.commit()
    return "ok"
