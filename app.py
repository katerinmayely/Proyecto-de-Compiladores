from flask import Flask, send_from_directory
import re

app = Flask(__name__)

@app.route('/') 
def index():
    print('Estamos en consola!!')
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug = True)