import datetime 

def cuanto_falta(fecha:str) -> float: 
    fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y')
    
    if fecha.month < 9 or (fecha.month == 9 and fecha.day < 21): 
        año = fecha.year
    else: 
        año = fecha.year + 1 
    
    comienzo_primavera = datetime.datetime(año,9,21)
    
    return (comienzo_primavera - fecha).days

if __name__ == '__main__':
    # fecha = input("Ingrese una fecha en formato dd/mm/AA: ")
    # print(f'Faltan {cuanto_falta(fecha)} días para la primavera')

    fecha = datetime.datetime(2020, 9, 26)
    print(fecha + 200)
