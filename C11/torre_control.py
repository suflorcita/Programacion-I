class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0 


class TorreDeControl(): 
    '''Modela el funcionamiento de una torre de control'''
    
    def __init__(self): 
        '''Crea una cola de arribos y de partidas'''
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, vuelo_arribo): 
        '''Agrega un vuelo a la lista de arribos'''
        self.arribos.encolar(vuelo_arribo) 

    def nueva_partida(self, vuelo_partida):
        '''Agrega un vuelo a la lista de partidas'''
        self.partidas.encolar(vuelo_partida)

    def ver_estado(self):
        '''Imprime el estado de la torre de Control'''
        print("Vuelos esperando para aterrizar: ", end="")  
        for vuelo in self.arribos.items: 
            print(vuelo, end="")
        
        print("\nVuelos esperando para despejar: ", end="") 
        for vuelo in self.partidas.items: 
            print(vuelo, end=" ")
    
    def asignar_pista(self): 
        '''Asigna pista para que los vuelos aterrizen o despeguen, con prioridad para los aterrizajes'''
        if not self.arribos.esta_vacia(): 
            aterrizaje = self.arribos.desencolar()
            print(f'El vuelo {aterrizaje} aterrizó con éxito.')
        elif not self.partidas.esta_vacia():
            despegue = self.partidas.desencolar()
            print(f'El vuelo {despegue} despegó con éxito.')
        else: 
            print('No hay vuelos en espera.')


# torre = TorreDeControl()
# torre.nuevo_arribo('AR156')
# torre.nueva_partida('KLM1267')
# torre.nuevo_arribo('AR32')
# torre.ver_estado()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
