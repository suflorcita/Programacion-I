def buscar_u_elemento(lista, elemento):
    '''Devuelve la posicion de la ultima aparicion del elemento en la lista
    '''
    pos = -1
    for i, z in enumerate(lista):
        if z == elemento:   # si encontramos a e
            pos = i  # guardamos su posición
                # y salimos del ciclo
    return pos

def buscar_n_elemento(lista, elemento):
    '''Devuelve la cantidad de elementos en la lista
    '''
    contador = 0
    for i in lista:
        if i == elemento:
            contador += 1
    return contador


def maximo(lista):
    '''Devuelve el máximo de una lista.
    ''' 
    try:
        m = lista[0] # m guarda el máximo de los elementos a medida que recorro la lista.
        for e in lista: # Recorro la lista y voy guardando el mayor
            if e > m: 
                m = e 
    except IndexError:
        print('La lista está vacía ')
        return None
    return m

def minimo(lista):
    '''Devuelve el mínimo de una lista.
    ''' 
    try:
        m = lista[0] # m guarda el minimo de los elementos a medida que recorro la lista.
        for e in lista: # Recorro la lista y voy guardando el mayor
            if e < m: 
                m = e 
    except IndexError:
        print('La lista está vacía ')
        return None
    return m