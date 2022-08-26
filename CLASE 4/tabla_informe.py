# Alumna:Sol Ayelen Cataldo 

import csv


def leer_camion(nombre_archivo): 
    camion = []
    
    with open(nombre_archivo,'rt') as f: 
        rows = csv.reader(f)
        headers = next(rows)
               
        for row in rows: 
            record = dict(zip(headers,  row)) # zipea los encabezados con las filas 
            lote = {}
            lote['nombre'] = record['nombre']
            lote['cajones'] = int(record['cajones'])
            lote['precio'] = float(record['precio'])
            camion.append(lote)
        
        return camion 
            

def leer_precios(nombre_archivo): 
    dict_fyv = {}
    
    with open(nombre_archivo,'rt') as f: 
        rows = csv.reader(f)
        for row in rows: 
            if row: 	# si la fila no está vacía 
                dict_fyv[row[0]] = float(row[1])
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


camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')

for nombre, cajones, precio, cambio in informe:
    precio = "$" + str(f'{precio:0.2f}')
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
