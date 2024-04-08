from flask import Flask
import re

app = Flask(__name__)

@app.route('/') 
def index():
    print('Estamos en consola!!')
    return 'Mi primer servidor en Python'

if __name__ == '__main__':
    app.run(debug = True)