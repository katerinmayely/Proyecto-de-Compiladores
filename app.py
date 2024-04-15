from flask import Flask, send_from_directory
import re
from analizador_sintactico import imprimir_arbol_sintactico_y_resultado
from analizador_lexico import convertir

app = Flask(__name__)

@app.route('/') 
def index():
    print('Estamos en consola!!')
    return send_from_directory('static', 'index.html')

def analisis_sintactico(entrada):
    return imprimir_arbol_sintactico_y_resultado(entrada)

@app.route('/analizando/<entrada>')
def analizar(entrada):
    
    #analisis léxico
    convertir(entrada)
    
    #analisis sintáctico
    return analisis_sintactico(entrada)

if __name__ == '__main__':
    app.run(debug = True)