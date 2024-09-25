#""ejersicio 1: crea una aplicacion web basica con flask que,al ser ejecutada, inicia un servidor local.
#en el puerto 5000 cuando visita la ruta principal (http://localhost:5000/)
#el servidaor respondera con un mensaje html que dice "hello, world flask"

# se importa el modulo flask desde el paquete flask
from flask import Flask

#crea una instancia de la clasflask
#el argumento __name__ le dicea flask
#que utilicceel el nombre del archivo actual main.py
app = Flask(__name__)

#este es un decorador que define una ruta 
#corresponde a la pagina del app
@app.route('/')
#cuando alguien visteapp (por ejemplo, http://localhost:5000)
#la funcion hello() sera ejecutada
def hello ():
    return "<h1>hello, world flask !</h1>"

#solo se ejecute si el archivo es ejecutado directamente
#arranca la aplicacion flask en modo de depuracion(debug=true)
if __name__ == '__main__':
    app.run(debug=True, port=5000)