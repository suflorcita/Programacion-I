#!/usr/bin/env python3
# informe_final.py

import csv
from fileparse import parse_csv
import formato_tabla

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

def imprimir_informe(informe, formateador):    
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    
    # encabezado 
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
     

    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

    pass

def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'): 
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)   

    # Crear los datos para el informe
    informe = hacer_informe(camion, precios)

    # Imprimir el informe 
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)
    pass 

def f_principal(parametros): 
    programa, archivo_camion, archivo_precios, fmt = parametros 
    informe_camion(archivo_camion, archivo_precios, fmt)
    pass


if __name__ == '__main__':
    import sys

    try:
        f_principal(sys.argv)
    except ValueError: 
        f_principal(['informe_final.py', '../Data/camion.csv', '../Data/precios.csv', "csv"])
    