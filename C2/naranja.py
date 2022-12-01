# Alumna: Sol Ayelen Cataldo 

costo_total = 0

f = open('../Data/precios.csv', 'rt')

for row in f: 
	row = row.strip().split(',')
	if row[0] == "Naranja": 
		precio_naranja = float(row[1])

f.close()

print('El precio de la Naranja es', precio_naranja)