# Alumna: Sol Ayelen Cayaldo 

def buscar_precio(fruta): 
	f = open('../Data/precios.csv', 'rt')
	existe_fruta = False

	for row in f: 
		row = row.strip().split(',')
		if row[0] == fruta: 
			precio = float(row[1])
			existe_fruta = True
			print("El precio de la", fruta, "es", precio)

	if not existe_fruta: 
		print(fruta, "no figura en el listado de precios")

	f.close()

	return precio 

 





