import csv
from collections import Counter 
import os 
import matplotlib.pyplot as plt
import numpy as np

def leer_parque(nombre_archivo, parque): 
    info_parque = []
    
    with open(nombre_archivo, 'rt') as f: 
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows: 
            record = dict(zip(headers, row))
            record['altura_tot'] = float(record['altura_tot'])
            record['inclinacio'] = int(record['inclinacio'])
            if record['espacio_ve'] == parque: 
                info_parque.append(record)

    return info_parque 

def especies(lista_arboles):
    especies = []
    for arbol in lista_arboles: 
        especies.append(arbol['nombre_com'])

    return set(especies)

def contar_ejemplares(lista_arboles):
    cant_especies = Counter()
    for arbol in lista_arboles: 
        cant_especies[arbol['nombre_com']] += 1 
    return cant_especies

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles: 
        if arbol['nombre_com'] == especie: 
            alturas.append(arbol['altura_tot'])

    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles: 
        if arbol['nombre_com'] == especie: 
            inclinaciones.append(arbol['inclinacio'])

    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    max_inclinacion = (-1, '')
    especies_arboles = especies(lista_arboles) # conjunto de especies sobre las que voy a iterar
    for arbol in especies_arboles: 
        especie_inclinaciones = obtener_inclinaciones(lista_arboles, arbol) #obtengo todas las inclinaciones
        if max(especie_inclinaciones) > max_inclinacion[0]: 
            max_inclinacion = (max(especie_inclinaciones), arbol)
    return max_inclinacion

def especie_promedio_mas_inclinada(lista_arboles):
    prom_max_inclinacion = (-1, '')
    especies_arboles = especies(lista_arboles) # conjunto de especies sobre las que voy a iterar
    for arbol in especies_arboles: 
        especie_inclinaciones = obtener_inclinaciones(lista_arboles, arbol) #obtengo todas las inclinaciones
        prom_inclinaciones = sum(especie_inclinaciones) / len(especie_inclinaciones) #promedio de todas las inclinaciones 
        if prom_inclinaciones > prom_max_inclinacion[0]: 
            prom_max_inclinacion = (prom_inclinaciones, arbol)
    return prom_max_inclinacion

def leer_arboles(nombre_archivo): 
    arboleda = []
    
    with open(nombre_archivo, 'rt') as f: 
        rows = csv.reader(f)
        headers = next(rows)

        arboleda = [dict(zip(headers, row)) for row in rows]
  
    return arboleda

def medidas_de_especies(especies,arboleda): 
    dict_especies = {}
    #dict_especies = {especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] 
    #                for especie in especies}
    # con compresión de diccionarios = inentendible 
    for especie in especies:
        valores_dict = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
        dict_especies[especie] = valores_dict    
    return dict_especies

def scatter_hd(lista_de_pares): 
    lista_de_pares = np.array(lista_de_pares)
    diametro = lista_de_pares[:,0]
    altura = lista_de_pares[:,1]
    
    plt.scatter(diametro, altura, alpha=0.3)
    plt.xlabel("Diámetro (cm)")
    plt.ylabel("Alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás") 
    plt.show()
    
    pass 


path = '../Data/arbolado-en-espacios-verdes.csv' 
# 5.16 

arboleda = leer_arboles(path)
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# print(H)

#5.17 

coordenadas_dyh = [(float(arbol['diametro']), float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# print(G[1], G[2])
# for row in G: 
#     print(row)

# 5.19
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
# verifico tener resultado esperado 
dict = medidas_de_especies(especies, arboleda)
for especie in especies: 
    print(len(dict[especie]))

# 6.10
plt.hist(altos, bins=100)
plt.show()

#6.11
scatter_hd(coordenadas_dyh)