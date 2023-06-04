from apps.User import bp_user
from flask import render_template, request, redirect
from flask_login import login_user
from utils.response import jsonify_response
from .user import User
from utils.db import db

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
    return jsonify_response(msg="成功")

@bp_user.route('/create_user', methods=["GET", "POST"])
def create():
    users = [
    User(uname="keyfall", upassword="zongming"),
    User(uname="佚名", upassword="")
        ]
    db.session.add_all(users)
    db.session.commit()
    return "ok"
