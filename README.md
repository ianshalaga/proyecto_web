Este repositorio es mi base de experimentación sobre desarrollo web.

# Requerimientos:

* Visual Studio Code (Editor de código):
    Linux: descargar el .deb desde la página web oficial (https://code.visualstudio.com/) y usar un gestor de paquetes para instalarlo (doble clic en caso de tener uno configurado por defecto).
    Windows: descargar el instalador e instalarlo.
* Python3:
    Linux: Suele venir instalado por defecto (si no: sudo apt install python3).
    Windows: https://www.python.org/
* Entornos virtuales de Python:
    Linux: sudo apt install python3-venv
* Administrador de paquetes de Python:
    Linux: sudo apt install python3-pip
* Git (Sistema de control de versiones):
    Linux: sudo apt install git
    Windows: https://git-scm.com/


# Pasos a seguir:

* Crear un repositorio en Github (https://github.com/). Esto implica tener una cuenta allí. Luego clonarlo en nuestro ordenador. Para ello nos paramos en la carpeta donde queramos clonarlo y ejecutamos: git clone <*url del repositorio*>
En Windows se puede utilizar el *Github Desktop* https://desktop.github.com/ y adminitrar todo el trabajo de manera gráfica.

* Dentro del directorio de nuestro repositorio creamos un entorno virtual: python3 -m venv venv. El propósito del entorno virtual es que todo lo que necesitemos instalar para nuestro proyecto solo se mantenga dentro del entorno del mismo y no afecte a todo el ordenador y a otros proyectos, es una manera más ordenada de trabajar y una buena práctica de trabajo. Para esto es necesario activar dicho entorno con: . venv/bin/activate , el punto (.) seguido de la ruta del *script* permite cargar en la consola dicho *script* de activación del entorno virtual.

* Instalar Flask: pip3 install flask

* A partir de aquí ya es posible comenzar a trabajar en el desarrollo de la web.