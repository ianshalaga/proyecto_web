# BIBLIOTECAS

from flask import Flask


# CUERPO

aplicacion_web = Flask(__name__) # Instancia de la clase Flask


# RUTAS

@aplicacion_web.route('/') # URL que activa la/s función/es definidas posteriormente
def hola_mundo():
    return "¡Hola mundo!"