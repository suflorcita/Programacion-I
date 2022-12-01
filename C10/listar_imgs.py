import os 
import sys

def archivos_png(directorio): 
    lista_png = []

    for root, dirs, files  in os.walk(directorio):
        for file in files:
            if file[-4:] == ".png": # el nombre del archivo termina con .png 
                lista_png.append(file)
    
    return lista_png 


if __name__ == "__main__":
    list_png = archivos_png(sys.argv[1]) # toma en la función el directorio que se ingresa por linea de comandos
    for png in list_png: 
        print(png)

