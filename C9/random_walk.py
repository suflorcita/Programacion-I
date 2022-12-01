import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rc('font', family='Comic Sans MS') # seteo fuente de los gráficos 

def randomwalk(largo):
    '''Genera una caminata al azar de N pasos de largo'''
    pasos=np.random.randint(-1,2,largo)    
    return pasos.cumsum()

def param_plot(titulo, subp=None, eje_x = "tiempo", eje_y = "distancia al origen"): 
    ''' Define los parámetros para los gráficos'''
    if subp: 
        x, y, z = subp # ubicación del subplot
        plt.subplot(x, y, z)
    
    plt.ylim(-700,700)
    plt.title(titulo)
    
    plt.xlabel(eje_x)
    plt.ylabel(eje_y)
    
    pass

if __name__ == '__main__':

    N = 100000
    colors = ['red', 'orange', 'yellow', 'chartreuse', 'green', 'springgreen', 
            'cyan', 'dodgerblue', 'blue', 'purple', 'violet', 'magenta']
    caminos = []

    plt.figure(figsize=(10,9)) 
    param_plot(titulo="12 caminatas al azar", subp=(2,1,1))
    
    for i in range(12): 
        camino = randomwalk(N)
        caminos.append(camino)
        plt.plot(camino, color = colors[i], alpha=0.8)

    camino_mas_alejado = np.argmax([np.mean(np.abs(cam)) for cam in caminos])
    camino_mas_proximo = np.argmin([np.mean(np.abs(cam)) for cam in caminos])

    param_plot(titulo="La caminata que más se aleja", subp=(2,2,3))
    plt.plot(caminos[camino_mas_alejado],color=colors[camino_mas_alejado])
    
    param_plot(titulo="La caminata que menos se aleja", subp=(2,2,4))
    plt.plot(caminos[camino_mas_proximo], color=colors[camino_mas_proximo])

    plt.show()

# aclaración: 
# aunque el enunciado da a entender que se pide la trayectoria 
# que posee el punto más alejado o más cercano al origen
# con un compañero pensamos que tiene más sentido graficar la trayectoria 
# que **en promedio** se alejó o se acercó más del origen 

