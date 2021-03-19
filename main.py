# BIBLIOTECAS

from flask import Flask, url_for


# CUERPO

aplicacion_web = Flask(__name__) # Instancia de la clase Flask


# RUTAS

@aplicacion_web.route('/') # URL que activa la/s función/es definidas posteriormente
def hola_mundo():
    return "¡Hola mundo!"

@aplicacion_web.route('/pagina2')
def pagina2():
    return "Página 2 XD"

@aplicacion_web.route('/<usuario>')
def pagina_usuario(usuario):
    return 'El usuario es %s' % usuario


# PRINCIPAL

if __name__ == '__main__':
    aplicacion_web.run(debug=True)