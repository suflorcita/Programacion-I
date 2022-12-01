#!/usr/bin/env python3
# informe_final.py

import csv
from fileparse import parse_csv

def leer_camion(nombre_archivo): 
    
    with open(nombre_archivo) as f:
        camion = parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion 
            

def leer_precios(nombre_archivo):
    
    with open(nombre_archivo) as f:
        lista_precios = parse_csv(f, types = [str, float], has_headers = False)
    
    dict_fyv = dict(lista_precios)
    
    return dict_fyv

def hacer_informe(cajones, precios): 
    informe = []

    for cajon in cajones: 
        linea_informe = ()
        fruta = cajon['nombre']
        cambio = abs(cajon['precio'] - precios[fruta])
        
        linea_informe = (cajon['nombre'], cajon['cajones'], cajon['precio'], cambio)
        informe.append(linea_informe)
    return informe  

def imprimir_informe(informe):     
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')

    for nombre, cajones, precio, cambio in informe:
        precio = "$" + str(f'{precio:0.2f}')
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

    pass

def informe_camion(nombre_archivo_camion, nombre_archivo_precios): 
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
    pass 

def f_principal(parametros): 
    programa, archivo_camion, archivo_precios = parametros 
    informe_camion(archivo_camion, archivo_precios)
    pass


if __name__ == '__main__':
    import sys

    try:
        f_principal(sys.argv)
    except ValueError: 
        f_principal(['informe_final.py', '../Data/camion.csv', '../Data/precios.csv'])
