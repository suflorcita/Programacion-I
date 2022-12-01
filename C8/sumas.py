def sumar_enteros1(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0.0 
    
    for i in range(desde, hasta +1): 
        suma += i

    return suma if desde - hasta != 0 else 0

def sumar_enteros2(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma =  ((hasta * (hasta + 1))/2) - (((desde - 1) * (desde))/2)
    
    return suma if desde - hasta != 0 else 0
