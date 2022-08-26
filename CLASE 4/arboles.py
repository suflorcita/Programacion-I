import csv
from collections import Counter 

def leer_parque(nombre_archivo, parque): 
    info_parque = []
    
    with open(nombre_archivo, 'rt') as f: 
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows: 
            record = dict(zip(headers, row))
            record['altura_tot'] = float(record['altura_tot'])
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



parque_general_paz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
# print(len(parque_general_paz))
# print(especies(parque_general_paz))

parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

for parque in parques: 
    
    arboles_parque = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)
    alturas_jacaranda = obtener_alturas(arboles_parque, 'Jacarandá')
    maximo_jacaranda = max(alturas_jacaranda)
    promedio_jacaranda = sum(alturas_jacaranda) / len(alturas_jacaranda)

    print(f'Las cinco especies más frecuentes en el parque {parque} son:')
    print(contar_ejemplares(arboles_parque).most_common(5))
    print(f'El promedio de alturas de los jacarandás es de: {promedio_jacaranda:0.2f} y el arbol con altura máxima mide {maximo_jacaranda:0.2f}')

