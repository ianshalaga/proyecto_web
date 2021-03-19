# BIBLIOTECAS

import os
from flask import Flask


# FUNCIONES

def crear_aplicacion(prueba_configuracion=None):
    '''
    Application factorty function
    '''
    aplicacion_web = Flask(__name__, instance_relative_config=True)
    aplicacion_web.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(aplicacion_web.instance_path, 'soul_calibur.sqlite'),
    )

    if prueba_configuracion is None:
        # Carga la instancia de configuración, si existe, cuando no se está en modo de pruebas
        aplicacion_web.config.from_pyfile('config.py', silent=True)
    else:
        # Carga la configuración de prueba pasada como parámetro
        aplicacion_web.config.from_mapping(prueba_configuracion)

    # Asegura que el directorio de la instancia existe
    try:
        os.makedirs(aplicacion_web.instance_path)
    except OSError:
        pass

    # Una página simple que dice Hola
    @aplicacion_web.route('/hola')
    def hola():
        return 'Hola mundo.'

    return aplicacion_web