# BIBLIOTECAS

import os
from flask import Flask


# FUNCIONES

def create_app(prueba_configuracion=None): # Esta función debe llamarse create_app
    '''
    Application factorty function
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'soul_calibur.sqlite'),
    )

    if prueba_configuracion is None:
        # Carga la instancia de configuración, si existe, cuando no se está en modo de pruebas
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carga la configuración de prueba pasada como parámetro
        app.config.from_mapping(prueba_configuracion)

    # Asegura que el directorio de la instancia existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Una página simple que dice Hola
    @app.route('/hola')
    def hola():
        return 'Hola.'

    from . import db # Incluye el archivo db.py desde el mismo directorio de este archivo
    db.init_app(app) # Inicializa la base de datos

    return app