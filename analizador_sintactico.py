from lark import Lark, Tree
from random import random, choice

# Gramática del lenguaje
gramatica = '''
    start: expr
    
    expr: entero destino
    
    destino: romano | hexadecimal | octal | binario | morse | aleatorio
    
    romano: "romano"i
    hexadecimal: "hexadecimal"i
    octal: "octal"i
    binario: "binario"i
    morse: "morse"i
    aleatorio: "aleatorio"i 
    
    entero: /\d+/
    
    %ignore /\s+/
'''
#Función para convertir de decimal a hexadecimal
def decimal_a_hexadecimal(numero):
    return hex(int(numero))[2:].upper()

#Función para convertir de decimal a octal
def decimal_a_octal(numero):
    return oct(int(numero))[2:]

#Función para convertir de decimal a binario
def decimal_a_binario(numero):
    return bin(int(numero))[2:]

#Función auxiliar para conversión a romano
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

#Función para convertir de decimal a romano   
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
 
#Función para convertir de decimal a código Morse 
def decimal_a_morse():
    pass
   
#Función para convertir de decimal a una base aleatoria
def decimal_a_aleatorio(numero):
    destinos = ['Hexadecimal', 'Octal', 'Binario', 'Romano', 'Morse']
    destino_aleatorio = choice(destinos)
    if destino_aleatorio == 'Hexadecimal':
        return 'Hexadecimal -> ' + decimal_a_hexadecimal(numero)
    elif destino_aleatorio == 'Octal':
        return 'Octal -> ' + decimal_a_octal(numero)
    elif destino_aleatorio == 'Binario':
        return 'Binario -> ' + decimal_a_binario(numero)
    elif destino_aleatorio == 'Romano':
        return 'Romano -> ' + decimal_a_romano(numero)
    elif destino_aleatorio == 'Morse':
        return 'Morse -> ' + decimal_a_morse(numero)

#Función para dar formato al árbol sintáctico        
def mostrar_arbol(tree, indent=0):
    if isinstance(tree, Tree):
        print(' ' * indent + str(tree.data))
        for child in tree.children:
            mostrar_arbol(child, indent + 4)
    else:
        print(' ' * indent + str(tree))

#Función que evalúa el árbol de análisis sintáctico, de acuerdo con reglas semánticas.
def evaluar(arbol):
    entero = arbol.children[0].children[0].children[0]
    valor_a_evaluar = arbol.children[0].children[1].children[0].data
    
    print('\n')
    if valor_a_evaluar == 'romano':
        print(decimal_a_romano(entero)) 
    elif valor_a_evaluar == 'hexadecimal':
        print(decimal_a_hexadecimal(entero) )
    elif valor_a_evaluar == 'octal':
        print(decimal_a_octal(entero)) 
    elif valor_a_evaluar == 'binario':
        print(decimal_a_binario(entero)) 
    elif valor_a_evaluar == 'morse':
        print(decimal_a_morse(entero)) 
    elif valor_a_evaluar == 'aleatorio':
        print(decimal_a_aleatorio(entero)) 

#Función para analizar sintácticamente una entrada e imprimir un árbol sintáctico.
def imprimir_arbol_sintactico_y_resultado(entrada):
    #Analizador Lark con la gramática
    parser = Lark(gramatica, start='start')
    
    arbol = parser.parse(entrada)
    
    #Imprimir el árbol sintáctico
    try:
        print("Árbol sintáctico:")
        mostrar_arbol(arbol)
        return evaluar(arbol)
    except Exception as e:
        print(e)
    