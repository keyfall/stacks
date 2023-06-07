from config import redb
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reload_database(app):
    redb_type = redb.get("type")
    if redb_type == 1:
        with app.app_context():
            db.drop_all()
            db.create_all()
    elif redb_type == 2:
        db.drop_all(app=app)
        db.create_all(app=app)
