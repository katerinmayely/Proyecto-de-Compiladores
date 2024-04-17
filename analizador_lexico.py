import re

#Inicio - Analizador Léxico
palabras_reservadas = ['Hexadecimal', 'Octal', 'Binario', 'Romano', 'Morse', 'Aleatorio']

def analizador_lexico(cadena):
    tokens = re.findall(r'(\d+)([A-Za-z]+)', cadena)
    for i, (numero, destino) in enumerate(tokens, start=1):
        yield i, numero, destino
#Fin - Analizador Léxico

def analisis_lexico(cadena):
    print('\nAnálisis Léxico')
    for linea, numero, destino in analizador_lexico(cadena):
        destinoValido = re.compile(r'(' + '|'.join(palabras_reservadas) + ')', re.IGNORECASE)
        coincidencia = destinoValido.search(destino)
        if coincidencia:
            print(f"+---------------------------------------------------------------+")
            print(f"|No. Línea : {linea} | Token Numero : {numero} | Token Destino: {destino} ")
        else:
            print(f"+---------------------------------------------------------------+")
            print(f"|No. Línea : {linea}   | Token Numero : {numero} | Token Error: {destino} |")
        print(f"+---------------------------------------------------------------+")
        
# Ejemplo de uso
# cadena = "300Romano /n592752900Octal /n592752900Decimal /n592752900Binario"
# convertir(cadena)