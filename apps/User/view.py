from apps.User import bp_user
from flask import render_template, request, redirect
from flask_login import login_user
from utils.response import jsonify_response
from .user import User


@bp_user.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return '''
                   <form action='/user/login' method='POST'>
                    <input type='text' name='uname' placeholder='email'/>
                    <input type='password' name='password' id='password' placeholder='password'/>
                    <input type='submit' name='submit'/>
                   </form>
                   '''

    uname =  request.form['uname']
    password =  request.form['password']
    user_results = User.query.filter_by(uname=uname, upassword=password)
    if len(user_results) <= 0:
        return 'Bad login'

    user = User()
    user.uname = uname
    login_user(user)
    return jsonify_response(msg="成功")