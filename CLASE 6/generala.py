import random 

def tirar(): 
    tirada = []

    for i in range(5): 
        tirada.append(random.randint(1, 6))
    return tirada

def es_generala(tirada):
    conj_tirada = set(tirada) 
    if len(conj_tirada) == 1: 
        return True 
    return False 


def prob_generala(N):   
    G = [sum([es_generala(i) for i in range(N )])]
    return prob 

N = 1
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N # probabilidad de tener generala servida 
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')


