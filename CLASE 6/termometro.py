import random 
import numpy as np 
import os

def medir_temp(n):
    mediciones = []
    for i in range(n):
        mediciones.append(random.normalvariate(0, 0.2) + 37.5)

    mediciones = np.array(mediciones)

    np.save('../Data/temperaturas', mediciones)

    return mediciones 

def resumen_temp(n):
    mediciones = medir_temp(n)
    mediciones.sort() # ordena de menor a mayor 

    maximo = max(mediciones)
    minimo = min(mediciones)
    promedio = sum(mediciones)/n

    if n % 2 != 0: #cantidad impar de medicciones 
        mediana = mediciones[n // 2]
    else: 
        mediana = (mediciones[n//2 - 1] + mediciones[n//2])/2
       
    return (maximo, minimo, promedio, mediana)


medir_temp(999)

#n = np.load('../Data/temperaturas.npy')
#print(n)