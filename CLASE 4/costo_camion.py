import csv
import sys

def costo_camion(nombre_archivo): 
    costo_total = 0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n_row, row in enumerate(rows, start=1): 
            record = dict(zip(headers,  row))
            try: 
                nro_cajones = int(record['cajones'])
                precio_cajones = float(record['precio'])
                costo_total += nro_cajones * precio_cajones
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError: 
                print(f'Fila {n_row}: No pude interpretar: {row}')

    return costo_total


costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)