import datetime 

def vida_en_segundos(fecha_nac:str) -> float:
    ''''Recibe una fecha en formato dd/mm/AAAA 
    y devuelve la cantidad en segundo hasta el momento que se ejecuta la función'''
    fecha_nac_object = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    tiempo_hasta_hoy = datetime.datetime.now() - fecha_nac_object
    return tiempo_hasta_hoy.total_seconds()

if __name__ == '__main__':
    fecha = input("Ingrese su fecha de nacimiento \n") 
    print(f'Viviste {vida_en_segundos(fecha)} segundos!! Felicitaciones!!!')

    