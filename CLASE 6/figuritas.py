import random
import numpy as np

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(A):
    return 0 in A

def comprar_figu(figus_total): 
    return random.randint(1, figus_total)

def cuantas_figus(figus_total): 
    n = 0
    album = crear_album(figus_total) 
    
    while album_incompleto(album): 
        figu = comprar_figu(figus_total)
        album[figu - 1] = 1 
        n += 1 

    return n

def experimento_figus(n_repeticiones, figus_total):
    repeticiones = [cuantas_figus(figus_total) for n in range(n_repeticiones)]
    return np.mean(repeticiones)


#print(experimento_figus(100, 670))