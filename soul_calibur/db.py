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
        g.db.row_factory = sqlite3.Row # Filas como diccionarios donde la clave es el nombre de la columna

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db') # Crea el comando init-db que llama a la función init_db()
@with_appcontext
def init_db_command():
    '''Limpia los datos existentes y crea nuevas tablas.'''
    init_db()
    click.echo('Base de datos inicializada.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)