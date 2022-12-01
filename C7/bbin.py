def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos


def donde_insertar(lista, x):
    '''Dónde insertar
    Recibe una lista ordenada y un elemento x 
    Devuelve la posición de ese elemento si está en la lista o
    la posición dónde se podría insertar el elemento. 
    '''
    
    izq = 0
    der = len(lista) - 1
    while izq <= der:        
        medio = (izq + der) // 2

        if lista[medio] == x:
            return medio     # elemento encontrado!

        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    if x > lista[medio]: 
        return medio + 1
 
    return medio


def insertar(lista, x): 
    if x in lista: 
        return busqueda_binaria(lista, x)
    else: 
        pos = donde_insertar(lista, x)
        lista = lista[0:pos] + [x] + lista[pos:]
        return lista 

