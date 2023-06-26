from flask import abort
from flask_login import current_user
from functools import wraps



def require_names(*names):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            print("username:", current_user.uname)
            if current_user.uname not in names:
                abort(403)
            return f(*args, **kwargs)
        return wrapped
    return wrapper