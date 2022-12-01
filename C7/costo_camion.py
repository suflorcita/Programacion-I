import csv
import sys
import informe_funciones

def costo_camion(nombre_archivo): 
    costo_total = 0
    
    costos = informe_funciones.leer_camion(nombre_archivo)

    for row in costos: 
        costo_total += row['cajones'] * row['precio']
        
    return costo_total


#costo = costo_camion('../Data/fecha_camion.csv')
#print('Costo total:', costo)

