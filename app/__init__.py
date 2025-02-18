import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)


from sqlalchemy.engine import Engine
from sqlalchemy import event

# Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    # record = db.Query(['SHOW TABLES']);
    print(db)
    cursor = dbapi_connection.cursor()
    test = cursor.execute("SHOW TABLES")
    print(test)
    cursor.close()

from . import models, views
