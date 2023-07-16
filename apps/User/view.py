from apps.User import bp_user
from flask import render_template, request, redirect, url_for, flash, make_response

from utils.login_utils import require_names
from .user import User
from apps.Book.book import Book
from utils.db import db
from flask_login import login_required, logout_user,login_user, current_user


@bp_user.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")


    uname =  request.form['uname']
    password =  request.form['password']
    user_result = User.query.filter_by(uname=uname, upassword=password).first()
    if not user_result:
        return '''
                    Bad login&nbsp;&nbsp;&nbsp;<a href='/user/login'>返回</a>
                '''

    user = user_result
    login_user(user, remember=True)

    #
    remember = True if request.form.get('remember') else False

    if user.uname=='佚名' :
        return render_template("upload.html", user = user)


    if user.uname!='keyfall' :
        context = searchbooks('1', '0', uname, user.id)
        return render_template("show_books.html", **context)

    context = searchbooks('0','0',uname, user.id)
    return render_template("audit.html", **context)

@login_required
def searchbooks(verify,logic_delete,uname, uid):
    if uid == 1:
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


@bp_user.route('/enroll', methods=["GET", "POST"])
def enroll():
    uname =  request.form['uname']
    password =  request.form['password']
    email =  request.form['email']
    user = User(uname=uname, upassword=password,email=email)
    db.session.add(user)
    flash(["已注册成功", "success"])

    return render_template('login.html')

@bp_user.route('/update_password', methods=["GET", "POST"])
@login_required
def update_password():
    if request.method == 'GET':
        return render_template('update_password.html',user=current_user)
    if current_user.uname=='佚名':
        return render_template("upload.html", user = current_user)
    password =  request.form['password']
    email =  request.form['email']
    user=current_user
    user.upassword = password
    user.email = email
    db.session.add(user)
    return render_template("login.html")
