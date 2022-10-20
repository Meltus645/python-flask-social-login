import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .constants import BASEDIR

def get_db(): 
    if not g.get('db'): 
        g.db =sqlite3.connect(BASEDIR /'sqlitedb.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory =sqlite3.Row
    return g.db

def close_db(e =None):
    db =g.pop('db', None)
    if db is not None: db.close()

def init_db():
    db =get_db()
    with current_app.open_resource(BASEDIR /'app/models/schema.sql') as f: db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clears all existing data and creates new tables"""
    init_db()
    click.echo("Database Initialized")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
        