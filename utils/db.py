from config import get_postgre_config as config
from flask_sqlalchemy import SQLAlchemy

db:SQLAlchemy = None

def init_db(app):
    global db
    db = SQLAlchemy(app)
    return db