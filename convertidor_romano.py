def construir_romano_menor4000(numero):
    if not isinstance(numero, int):
        return "Error: Ingresa un número entero"
    
    if numero <= 0:
        return ""
    
    valores_decimales = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos_romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numero_romano = ''
    i = 0
    
    while numero > 0:
        if numero - valores_decimales[i] >= 0:
            numero_romano += simbolos_romanos[i]
            numero -= valores_decimales[i]
        else:
            i += 1
            
    return numero_romano


def contar_miles(numero):
   
    veces_mil = 0
    while numero >= 1000:
       
        if numero % 1000 == 0:
            veces_mil += 1
            numero //= 1000
            
        else:
            numero -= 1
    return veces_mil


def convertir_a_romano(number):
    romano=''
    numero= int(number)
    if numero < 4000:
        romano = construir_romano_menor4000(numero)
    else:
        romano= construir_romano_mayor_igual4000(numero)
    return romano
    

def construir_romano_mayor_igual4000(numero):
    contarMiles=contar_miles(numero)
    numero_romano = ''
    numeroEvaluar=numero
    array=[]
    unidadEvaluar= numeroEvaluar//(1000**contarMiles)
    contador=contarMiles
    if unidadEvaluar<4:
        contador=contarMiles-1

    for i in range(contador,0,-1):
        unidad= numeroEvaluar//(1000**i)
        quitarUnidad= unidad *(1000**i)
        array.append(unidad)
        numeroEvaluar = numeroEvaluar-quitarUnidad
        if i==1:
            array.append(numeroEvaluar)
    
    
    for i in range(len(array)):
        cantidadRayas=len(array)-(i+1)
        rayas='\u0305' * cantidadRayas
        numeroRomanoUnidad = construir_romano_menor4000(array[i])
        romanoConRayas= ''.join(simbolo + rayas for simbolo in numeroRomanoUnidad)
        numero_romano += romanoConRayas

    return numero_romano

