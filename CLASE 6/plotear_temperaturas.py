import matplotlib.pyplot as plt
import numpy as np

def plotear_test(): 
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas, bins=25)
    plt.show()
    pass

plotear_test()