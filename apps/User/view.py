from apps.User import bp_user
from flask import render_template,request
from utils.response import jsonify_response
from user import User

@bp_user.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return '''
                   <form action='login' method='POST'>
                    <input type='text' name='uname' placeholder='email'/>
                    <input type='password' name='password' id='password' placeholder='password'/>
                    <input type='submit' name='submit'/>
                   </form>
                   '''

    uname =  request.form['uname']
    password =  request.form['password']



    if email in users and flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'