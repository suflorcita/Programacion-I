#soluciones_de_errores.py 
# Ejercicios de errores en el código 

#%%
#Ejercicio 3.5: Semántica
#Comentario: El error era de tipo semántico. Evalúa solo la primera letra.   
#Lo corregí poniendo una bandera que cambia de False a True si encuentra 
# una "a" en la expresión. 

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    minuscula = False 
    while i<n:
        if expresion[i] == 'a':
            minuscula = True
        i += 1
    return minuscula 


#%%
#Ejercicio 3.6: Sintaxis
#Comentario: El error era de tipo sintáctico. Faltan ":", falta un "=" en la 
#comparación y está mal escrita la palabra False
#Lo solucioné corrigiendo los errores de sintaxis
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))



#%%
#Ejercicio 3.7: Tipos
#Comentario: El error era de tipo tiempo de ejecución ya que se intenta
#  evaluar un tipo de dato int como si fuera una string 
#Lo corregí convirtiendo la expresión en una string 

def tiene_uno(expresion): 
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

#%%
#Ejercicio 3.8: Alcances
#Comentario: El error era de tipo semántico. 
#El resultado no era el esperado porque faltaba retornar algún valor
#Lo corregí agregando un return.

def suma(a,b):
    c = a + b
    return c 

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.9: pisando memoria 
#Comentario: Agrego a la variable camion, la informaciòn de la variable registro 
# pero esta variable se sobreescribe a cada linea y termino agregando muchas veces 
# veces la ultima fila del archivo. 

# Lo solucioné redefiniendo la variable registro como un
#  diccionario vacio en cada iteración 
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)            
        
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
