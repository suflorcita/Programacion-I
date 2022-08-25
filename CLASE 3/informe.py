# Alumna:Sol Ayelen Cataldo 

import csv


def leer_camion(nombre_archivo): 
	camion = []

	with open(nombre_archivo,'rt') as f: 
		rows = csv.reader(f)
		headers = next(rows)

		for row in rows: 
			lote = {}
			lote['nombre'] = row[0]
			lote['cajones'] = int(row[1])
			lote['precio'] = float(row[2])
			camion.append(lote)


	return camion 

def leer_precios(nombre_archivo): 
	dict_fyv = {}

	with open(nombre_archivo,'rt') as f: 
		rows = csv.reader(f)
		for row in rows: 
			if row: 	
				dict_fyv[row[0]] = float(row[1])

	return dict_fyv



total_compra = 0 # precio que pago al productor de frutas 
total_recaudado = 0  # precio total que recaudo con las ventas

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')

for fruta in camion: 
	total_compra += fruta['cajones'] * fruta['precio']
	total_recaudado += fruta['cajones'] * precios[fruta['nombre']]

diferencia = total_recaudado - total_compra

if diferencia > 0: 
	balance = 'ganancia'
else: 
	balance = 'perdida'
	
print(f'El camion costó ${total_compra}, recaudó un total de ${total_recaudado} y tuvo una {balance} de ${abs(diferencia):.2f}')

# salida: El camion costó $47671.15, recaudó un total de $62986.1 y tuvo una ganancia de $15314.949999999997
