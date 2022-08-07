# Alumna: Sol Ayelen Cataldo 

costo_total = 0

f = open('../Data/camion.csv', 'rt')

headers = next(f).strip().split(',') 
# strip elimina el "/n"

for row in f: 
	row = row.strip().split(',')
	nro_cajones = int(row[1])
	precio_cajones = float(row[2])
	costo_total += nro_cajones * precio_cajones

f.close()

print('Costo total', costo_total)