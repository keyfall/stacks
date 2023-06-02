from config import get_postgre_config as config
# from psycopg_pool import NullConnectionPool
from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    db = SQLAlchemy(app)

    return db