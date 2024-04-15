from lark import Lark, Tree
from random import random, choice
from analizador_lexico import convertir, decimal_a_aleatorio, decimal_a_binario, decimal_a_hexadecimal, decimal_a_octal, decimal_a_romano

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
        return str(decimal_a_romano(entero)) 
    elif valor_a_evaluar == 'hexadecimal':
        return str(decimal_a_hexadecimal(entero) )
    elif valor_a_evaluar == 'octal':
        return str(decimal_a_octal(entero)) 
    elif valor_a_evaluar == 'binario':
        return str(decimal_a_binario(entero)) 
    elif valor_a_evaluar == 'morse':
        #print(decimal_a_morse(entero)) 
        pass
    elif valor_a_evaluar == 'aleatorio':
        return str(decimal_a_aleatorio(entero)) 

#Función para analizar sintácticamente una entrada e imprimir un árbol sintáctico.
def imprimir_arbol_sintactico_y_resultado(entrada):
    #Analizador Lark con la gramática
    parser = Lark(gramatica, start='start')
    
    arbol = parser.parse(entrada)
    
    #Imprimir el árbol sintáctico
    try:
        print("\nAnálisis Sintáctico")
        print("Árbol sintáctico:")
        mostrar_arbol(arbol)
    except Exception as e:
        print(e)
        
    return str(evaluar(arbol))
    