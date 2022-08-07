# Alumna: Sol Ayelen Cataldo 

import csv

def costo_camion(nombre_archivo): 
	costo_total = 0

	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows: 
			try: 
				nro_cajones = int(row[1])
				precio_cajones = float(row[2])
				costo_total += nro_cajones * precio_cajones
			except ValueError: 
				print("La fila presenta valores no válidos")

	return costo_total

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)