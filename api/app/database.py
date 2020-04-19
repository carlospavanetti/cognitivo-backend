from flask import current_app
from sqlalchemy import create_engine, select, MetaData, Table


def connection(app):
    engine = app.config.get('DB') or create_engine(app.config['DATABASE_URI'])
    app.config.update(DB=engine)
    return engine


def select_all(table):
    con = connection(current_app).connect()
    query = Table(table, MetaData(), autoload=True, autoload_with=con)
    return con.execute(select([query])).fetchall()
