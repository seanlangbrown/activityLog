from pymongo import MongoClient

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.client = MongoClient('mongodb://localhost:27017/')
        g.db = g.client['vectorcare']
        # g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    client = g.pop('client', None)

    if client is not None:
        client.close()

def insert_event(event):
    db = get_db()
    db.insert_one(event)

def query_events(params):
    db = get_db()
    # TODO: return db.find()
    return [{'type': 'test', 'user_id': 1000, 'time': '00:00:00', 'data': {'other': 'unknown'}}]


def init_app(app):
    app.teardown_appcontext(close_db)

# def init_db():
#     db = get_db()