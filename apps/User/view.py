from apps.User import bp_user
from flask import render_template, request, redirect, url_for
from flask_login import login_user

from utils.login_utils import require_names
from .user import User
from apps.Book.book import Book
from utils.db import db
from flask_login import login_required, logout_user


@bp_user.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return '''
                   <form action='/user/login' method='POST'>
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
    if user.uname=='佚名' :
        return render_template("upload.html", user = user)


    if user.uname!='keyfall' :
        context = searchbooks('1', '0', uname, user.id)
        return render_template("show_books.html", **context)

    context = searchbooks('0','0',uname, user.id)
    return render_template("audit.html", **context)

@login_required
def searchbooks(verify,logic_delete,uname, uid):
    if uid=='1':
        pagination = Book.query.filter_by(verify=verify, logic_delete=logic_delete).order_by(
            Book.create_time.desc()).paginate(page=1, per_page=10, error_out=False)
    else:
        pagination = Book.query.filter_by(verify=verify, logic_delete=logic_delete, user_id=uid).order_by(Book.create_time.desc()).paginate(page=1,per_page=10,error_out=False)
    books = pagination.items
    context = {
        "books":books,
        "uname":uname,
        "pagination": pagination
    }
    return context


@bp_user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))

@bp_user.route('/go_upload')
@login_required
@require_names(("keyfall"))
def go_upload():
    context = searchbooks('1', '0', 'keyfall', '1')
    return render_template("show_books.html", **context)

@bp_user.route('/create_user', methods=["GET", "POST"])
def create():
    users = [
    User(uname="keyfall", upassword="zongming"),
    User(uname="佚名", upassword=""),
    User(uname="test", upassword="test"),
    ]
    db.session.add_all(users)
    db.session.commit()
    return "ok"
