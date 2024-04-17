import random
import convertidor_romano

#Función para convertir un número decimal a hexadecimal.
def decimal_a_hexadecimal(numero):
    return hex(int(numero))[2:].upper()

#Función para convertir un número decimal a octal.
def decimal_a_octal(numero):
    return oct(int(numero))[2:]

#Función para convertir un número decimal a binario.
def decimal_a_binario(numero):
    return bin(int(numero))[2:]

#Función para convertir un número entero a código Morse.
def decimal_a_morse(numero):
    # Definimos un diccionario que mapea cada dígito del número a su equivalente en código Morse
    morse_code = {
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    # Creamos una lista vacía para almacenar los códigos Morse de los dígitos
    codigo_morse = []
    # Iteramos sobre cada dígito en el número ingresado por el usuario
    for digito in numero:
        # Verificamos si el dígito es un número (isdigit() devuelve True si el dígito es un número)
        if digito.isdigit():
            # Si el dígito es un número, añadimos su equivalente en código Morse a la lista
            codigo_morse.append(morse_code[digito])
    # Finalmente, unimos los códigos Morse de los dígitos con un espacio y devolvemos el resultado como una cadena
    return ' '.join(codigo_morse)

#Función para convertir un número decimal entero a romano.
def decimal_a_romano(n):
    return convertidor_romano.convertir_a_romano(n)

#Función para convertir un número decimal a cualquiera de los formatos anteriores.
def decimal_a_aleatorio(numero):
    destinos = ['Hexadecimal', 'Octal', 'Binario', 'Romano', 'Morse']
    destino_aleatorio = random.choice(destinos)
    if destino_aleatorio == 'Hexadecimal':
        return 'Hexadecimal - ' +  decimal_a_hexadecimal(numero)
    elif destino_aleatorio == 'Octal':
        return 'Octal - ' +  decimal_a_octal(numero)
    elif destino_aleatorio == 'Binario':
        return 'Binario - ' +  decimal_a_binario(numero)
    elif destino_aleatorio == 'Romano':
        return 'Romano - ' + decimal_a_romano(numero)
    elif destino_aleatorio == 'Morse':
        return 'Morse - ' + decimal_a_morse(numero)