#!/usr/bin/env python3
# costo_camion.py
import csv
import sys
import informe_final

def costo_camion(nombre_archivo): 
    costo_total = 0
    
    costos = informe_final.leer_camion(nombre_archivo)
     
    for row in costos: 
        costo_total += row['cajones'] * row['precio']
        
    return costo_total

def f_principal(parametros):
    programa, nombre_archivo = parametros 
    costo = costo_camion(nombre_archivo)
    print('Costo total:', costo)


if __name__ == '__main__':
    import sys
    
    try:
        f_principal(sys.argv)
    except ValueError: 
        f_principal(['costo_camion.py', '../Data/camion.csv'])
    

