# Alumna:Sol Ayelen Cataldo 

import csv

def leer_camion(nombre_archivo): 
	camion = []

	with open(nombre_archivo,'rt') as f: 
		rows = csv.reader(f)
		headers = next(rows)

		for row in rows: 
			lote = (row[0], int(row[1]), float(row[2]))
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


# calculo lo que costó el camión 
costo_camion = 0
total_recaudado = 0 

camion = leer_camion("../Data/camion.csv")
for fruta in camion: 
	costo_camion += fruta[1] * fruta[2]
	total_recaudado += 

print(total_recaudado - costo_camion)