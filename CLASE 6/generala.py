import random 
from collections import Counter 

def tirar(N): 
    '''Devuelve una lista con N dados generados aleatoriamente'''
    tirada = []

    for i in range(N): 
        tirada.append(random.randint(1, 6))
    return tirada



def es_generala(tirada):
    '''Devuelve True si los cinco dados son iguales'''
    conj_tirada = set(tirada) 
    if len(conj_tirada) == 1: 
        return True 
    return False 


def prob_generala(N):   
    '''Devuelve la probabilidad de obtener una generala al finalizar una mano de tres tiradas 
        para una simulación de N elementos'''
        
    suma = 0 
    for i in range(N): 
        # empiezo el juego 
        generala = False
        n = 0 # dados que tengo guardado 
        
        for tirada in range(3):
            dados_tirada = tirar(5 - n) # tiro los dados que me quedan por tirar 
            conteo = Counter(dados_tirada)    # cuento los valores dentro de la tirada
            
            if tirada == 0: # en la primera tirada elijo un valor 
                valor_guardado = conteo.most_common(1)[0][0] # numero del dado guardado 
                n = conteo.most_common(1)[0][1] # cantidad de veces que salio 

            else: # en las otras dos tiradas compara 
                if valor_guardado in conteo: 
                    n += conteo[valor_guardado] 
        
            if n == 5: generala = True
        # termino el juego 

        suma += generala 
    
    return suma/N



print(prob_generala(10000))
