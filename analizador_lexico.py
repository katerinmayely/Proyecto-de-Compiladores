import re
import random

#Inicio - Analizador Léxico
palabras_reservadas = ['Hexadecimal', 'Octal', 'Binario', 'Romano', 'Alternativo', 'Aleatorio']

def analizador_lexico(cadena):
    tokens = re.findall(r'(\d+)([A-Za-z]+)', cadena)
    for i, (numero, destino) in enumerate(tokens, start=1):
        yield i, numero, destino
#Fin - Analizador Léxico

def decimal_a_hexadecimal(numero):
    return hex(int(numero))[2:].upper()

def decimal_a_octal(numero):
    return oct(int(numero))[2:]

def decimal_a_binario(numero):
    return bin(int(numero))[2:]
    
def decimal_a_morse(numero):
    pass

def modulo_de_numeros_romanos(numero,resultado_romano,bloque):
    valores_romanos = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    simbolos_romanos = sorted(valores_romanos.items(), reverse=True)
    
    resultado_romano
    i = 0
    entro=False
    while numero > bloque-1:
        entro=True
        valor, simbolo = simbolos_romanos[i]
        if valor*bloque<= numero:
            resultado_romano += simbolo
            numero -= valor*bloque
        else:
            i += 1
    if entro:
        repetir=0
        while bloque%1000==0:
            repetir+=1
            bloque=bloque/1000
        while repetir>0:
            resultado_romano+='|'
            repetir-=1
            

    return numero,resultado_romano
    
def decimal_a_romano(n):
    numero = int(n)
    cantidad_bloques = int(n)
    resultado_romano = ''
    bloque=1
    
    while cantidad_bloques/1000>1:
        bloque=bloque*1000
        cantidad_bloques=cantidad_bloques/1000
        
    if numero >= 4*bloque:
        while bloque/1000>=1:
            numero,resultado_romano=modulo_de_numeros_romanos(numero,resultado_romano,bloque)
            bloque=bloque/1000
            
    elif bloque>1:
        bloque=bloque/1000
        while bloque>=1:
            numero,resultado_romano=modulo_de_numeros_romanos(numero,resultado_romano,bloque)
            bloque=bloque/1000
    else:
        numero,resultado_romano=modulo_de_numeros_romanos(numero,resultado_romano,1)
        
    return resultado_romano
    

def decimal_a_aleatorio(numero):
    destinos = ['Hexadecimal', 'Octal', 'Binario', 'Romano']
    destino_aleatorio = random.choice(destinos)
    if destino_aleatorio == 'Hexadecimal':
        return decimal_a_hexadecimal(numero)
    elif destino_aleatorio == 'Octal':
        return decimal_a_octal(numero)
    elif destino_aleatorio == 'Binario':
        return decimal_a_binario(numero)
    elif destino_aleatorio == 'Romano':
        return decimal_a_romano(numero)

def convertir(cadena):
    print('\nAnálisis Léxico')
    for linea, numero, destino in analizador_lexico(cadena):
        destinoValido = re.compile(r'(' + '|'.join(palabras_reservadas) + ')')
        coincidencia = destinoValido.search(destino)
        if coincidencia:
            print(f"+---------------------------------------------------------------------+")
            print(f"|No. Línea : {linea} | Token Numero : {numero} | Token Destino: {destino} ")

            if destino == 'Hexadecimal':
                print(f"+---------------------------------------------------------------------+")
                print(f"| Cadena: {numero}{destino} | Salida: {decimal_a_hexadecimal(numero)}                     |")
                print(f"+---------------------------------------------------------------------+")
                
            elif destino == 'Octal':
                print(f"+---------------------------------------------------------------------+")
                print(f"| Cadena: {numero}{destino}  | Salida: {decimal_a_octal(numero)}                        |")
                print(f"+---------------------------------------------------------------------+")
                 
            elif destino == 'Binario':
                print(f"+---------------------------------------------------------------------+")
                print(f"| Cadena: {numero}{destino}  | Salida: {decimal_a_binario(numero)}  |")
                print(f"+---------------------------------------------------------------------+")
               
            elif destino == 'Romano':
                
                print(f"+---------------------------------------------------------------------+")
                print(f"| Cadena: {numero}{destino}  | Salida: {decimal_a_romano(numero)}               |")
                print(f"+---------------------------------------------------------------------+")
                
            elif destino == 'Aleatorio':
                print(f"+-------------------------------------------------------------------------")
                print(f"| Cadena: {numero}{destino}  | Salida: {decimal_a_aleatorio(numero)}     |")
                print(f"+-------------------------------------------------------------------------")
     
            elif destino == 'Morse':
                print(f"+-------------------------------------------------------------------------")
                print(f"| Cadena: {numero}{destino}  | Salida: {decimal_a_morse(numero)}         |")
                print(f"+-------------------------------------------------------------------------")
        else:
            print(f"+---------------------------------------------------------------------+")
            print(f"|No. Línea : {linea}   | Token Numero : {numero} | Token Error: {destino} |")
        
# Ejemplo de uso
cadena = "1592752900Romano /n592752900Octal /n592752900Decimal /n592752900Binario"
convertir(cadena)
