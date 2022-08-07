# Alumna: Sol Ayelen Cataldo

prueba = ['banana', 'manzana', 'mandarina']

def pasar_geringoso(palabra): 
	capadepenapa = ''
	vocales = ['a','e','i','o','u']
	i = 0

	for c in palabra:
	    capadepenapa += c
	    if c in vocales: 
	       capadepenapa = capadepenapa + 'p' + c

	return capadepenapa


def diccionario_geringoso(palabras): 
	dict_geringoso = {}

	for palabra in palabras: 
		dict_geringoso[palabra] = pasar_geringoso(palabra)
	
	return dict_geringoso


prueba_geringoso = diccionario_geringoso(prueba)
print(prueba_geringoso)  