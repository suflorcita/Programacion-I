import csv
from collections import Counter 
from os import getcwd

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

path = '../Data/arbolado-en-espacios-verdes.csv' 

parque_general_paz = leer_parque(path, 'GENERAL PAZ')
# print(len(parque_general_paz))
# print(especies(parque_general_paz))

parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

# imprimo los resultados en pantalla 
for parque in parques: 
    arboles_parque = leer_parque(path, parque)
    especies_mas_comunes = contar_ejemplares(arboles_parque).most_common(5)
   
    alturas_jacaranda = obtener_alturas(arboles_parque, 'Jacarandá')
    maximo_jacaranda = max(alturas_jacaranda)
    promedio_jacaranda = sum(alturas_jacaranda) / len(alturas_jacaranda)
   
    mayor_inclinacion = especimen_mas_inclinado(arboles_parque)
    mayor_inclinacion_promedio =  especie_promedio_mas_inclinada(arboles_parque)

    print(f'Las cinco especies más frecuentes en el parque {parque} son:')
    
    for especies_comunes in especies_mas_comunes:
        print(f'La especie {especies_comunes[0]} con {especies_comunes[1]} ejemplares')
   
    print(f'El promedio de alturas de los jacarandás es de: {promedio_jacaranda:0.2f} m y el arbol con altura máxima mide {maximo_jacaranda:0.2f} m')
    print(f'La especie con el ejemplar más inclinado es {mayor_inclinacion[1]}  y está inclinada {mayor_inclinacion[0]} grados.')
    print(f'La especie que está en promedio más inclinada es {mayor_inclinacion_promedio[1]} y está inclinada {mayor_inclinacion_promedio[0]} grados')