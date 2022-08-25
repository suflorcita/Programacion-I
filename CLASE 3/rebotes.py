# Alumna: Sol Ayelen Cataldo 
import sys

if len(sys.argv) > 1: 
    print(len(sys.argv))
    altura = float(sys.argv[1])
else: 
    altura = 100

for i in range(10):
    altura = 3/5 * altura
    print(i+1, round(altura,4))
    
