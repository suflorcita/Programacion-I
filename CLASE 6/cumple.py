import random 

def cumpleaños(x): 
    '''Retorna True si de x personas, dos cumplen el mismo dia '''
    cump = [random.randint(1, 365) for i in range(x)] # cumpleaños de las personas 
    if len(set(cump)) != x: 
        return True
    
    return False 

def prob_cumpleaños(N, x): 
    '''Retorna la probabilidad numérica de que dos personas de x cumplan el mismo dia 
       usando N eventos '''
    S = sum([cumpleaños(x) for i in range(N)])
    prob = S/N 
    return prob

for i in range(1, 100, 5): 
    print(f'Considerando 10000 ensayos, para {i} personas')
    print(f'La probabilidad de que dos personas cumplan el mismo día es de {prob_cumpleaños(10000, i)}') 