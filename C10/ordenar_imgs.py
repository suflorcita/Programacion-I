import os 
import sys
import datetime
import time 

# correr como
# python3 ordenar_imgs.py ../Data/ordenar/ ../Data/imgs_procesadas/

def procesar_nombre(fname): 
    '''Recibe el nombre de un archivo PNG en el que los ultimos 8 caracteres 
    tienen la fecha en formato AAAAMMDD y retorna esa fecha (formato datetime) y un nuevo nombre del archivo sin la fecha.'''
    fecha = fname[-12:-4] 
    fecha_object = datetime.datetime.strptime(fecha, '%Y%m%d') # convierto la fecha a un objeto datetime 
    
    nombre_corregido = fname[:-13] + ".png"
    return nombre_corregido, fecha_object 

def procesar(fname, destino = "../Data/imgs_procesadas"):
    '''Recibe la ruta de un archivo PNG junto a un directorio de destino. El archivo PNG tiene en los últimos 8 caracteres de su nombre la fecha en formato AAAAMMDD.  
    Renombra y mueve el archivo al directorio de destino. 
    Elimina la fecha del titulo y la usa para setearla como fecha de modificacion y acceso del archivo'''

    nuevo_nom_png, nuevo_fecha_png = procesar_nombre(fname) 

    # seteo la fecha de modificacion y acceso 
    ts_acceso = nuevo_fecha_png.timestamp()
    ts_modifi = nuevo_fecha_png.timestamp()
    os.utime(fname, (ts_acceso, ts_modifi))

    # defino la ruta a la nueva carpeta 
    nom_png = nuevo_nom_png.split('/')[-1]
    new_path_png = os.path.join(destino, nom_png)
    
    # renombro y muevo el archivo
    os.rename(fname, new_path_png)

    pass

# if __name__ == "__main__":
#     dir_a_leer = sys.argv[1]
#     dir_destino = sys.argv[2]

#     if not os.path.exists(dir_destino): 
#         os.makedirs(dir_destino) # crea el directorio si no existe

#     for root, dirs, files  in os.walk(dir_a_leer):
#         for file in files:
#             if file[-4:] == ".png": # el nombre del archivo termina con .png 
#                 path_png = os.path.join(root, file) # ruta del archivo
#                 procesar(path_png, dir_destino)
    
#     # borra los directorios que estan vacíos       
#     for root, dirs, files in os.walk(dir_a_leer):
#         for dir in dirs: 
#             path_dir = os.path.join(root, dir)
#             if len(os.listdir(path_dir)) == 0: 
#                 os.rmdir(path_dir)
