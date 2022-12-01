def valor_absoluto(n):
    ''' Devuelve el valor absoluto de un número n. 
    Pre: n es una variable entera o flotante 
    Pos: devuelve el valor absoluto de n 
    '''
    
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    ''' Calcula la suma de los elementos pares en la lista l 
    Pre: l debe ser una lista con elementos enteros
    Pos: devuelve la suma de los elementos pares en la lista l. 

    En este caso el invariante de ciclo es que res contiene la suma de los elementos pares en la lista. 
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    ''' Calcula el producto entre a y b
    Pre: a debe ser un número entero o flotante y b debe ser un número entero positivo 
    Pos: devuelve el producto entre a y b          
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):
    '''Devuelve la cantidad de términos en la sucesión de collatz de un número n. 
    Pre: n es un número entero positivo 
    Cons: devuelve un entero que representa la cantidad de términos en la sucesión de Collatz. 
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res