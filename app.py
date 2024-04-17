from flask import Flask, send_from_directory
from analizador_sintactico import imprimir_arbol_sintactico_y_resultado
from analizador_lexico import analisis_lexico

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
    analisis_lexico(entrada)
    
    #analisis sintáctico
    salida = analisis_sintactico(entrada)
    
    return salida

if __name__ == '__main__':
    app.run(debug = True)