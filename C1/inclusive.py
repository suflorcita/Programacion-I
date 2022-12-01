# Alumna: Sol Ayelen Cataldo 

frase = 'Todos, tu también'
palabras = frase.split()
frase_t = ''

for palabra in palabras:  
    if palabra.endswith('o'):
        palabra = palabra[:len(palabra)-1] + 'e'
    elif palabra.endswith('os'): 
        palabra = palabra[:len(palabra)-2] + 'es'
        
    frase_t += palabra + ' '
    
print(frase_t)

# Hay dos problemas 
# En palabras que terminan en O pero no son masculinas, también las convierte. Este problema no sé solucionarlo 
# En palabras a las que sigue la coma, toma la coma como la ultima letra. Este problema si lo puedo solucionar, 
# rastreando los posibles signos de puntuación y agregando un if. (Debería pensarlo un poco más)
        
