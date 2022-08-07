# Alumna: Sol Ayelén Cataldo 

cadena = 'Geringoso'
capadepenapa = ''
vocales = ['a','e','i','o','u']
i = 0

for c in cadena:
    capadepenapa += c
    if c in vocales: 
       capadepenapa = capadepenapa + 'p' + c

print(capadepenapa)
      