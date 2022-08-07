# Alumna: Sol Ayelen Cataldo 

import csv

def costo_camion(nombre_archivo): 
	costo_total = 0

	f = open(nombre_archivo, 'rt')

	rows = csv.reader(f)

	headers = next(rows)

	for row in rows: 
		nro_cajones = int(row[1])
		precio_cajones = float(row[2])
		costo_total += nro_cajones * precio_cajones

	f.close()

	return costo_total

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)