# BIBLIOTECAS

import sqlite3

import click
from flask import current_app, g
'''
g es un objeto especial que es único para cada solicitud.
Se utiliza para almacenar datos a los que pueden acceder múltiples
funciones durante la solicitud.
La conexión se almacena y se reutiliza en lugar de crear una nueva
conexión si se llama a get_db por segunda vez en la misma solicitud.
'''
from flask.cli import with_appcontext


# FUNCIONES

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()