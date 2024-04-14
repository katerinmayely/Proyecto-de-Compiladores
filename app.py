from flask import Flask, send_from_directory
import re
from analizador_sintactico import imprimir_arbol_sintactico_y_resultado

app = Flask(__name__)

def convertir_a_morse(num):
    pass

@app.route('/k') 
def hola():
    print('Estamos en consola!!')
    return 'Hola'

@app.route('/') 
def index():
    print('Estamos en consola!!')
    return send_from_directory('static', 'index.html')

def analisis_lexico(entrada):
    pass

def analisis_sintactico(entrada):
    imprimir_arbol_sintactico_y_resultado(entrada)
    pass

@app.route('/analizando/<entrada>')
def analizar(entrada):
    #analisis_lexico(entrada)
    analisis_sintactico(entrada)

if __name__ == '__main__':
    app.run(debug = True)