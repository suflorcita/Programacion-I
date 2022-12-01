import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import os 


if __name__ == '__main__':
    directorio = '../Data'
    archivo = 'arbolado-publico-lineal-2017-2018.csv'

    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

    fname = os.path.join(directorio,archivo)
    df = pd.read_csv(fname, low_memory=False)[cols_sel]

    #print(df['nombre_cientifico'].value_counts().head(10)) # imprimo las 10 especies más frecuentes 

    df_seleccion = df[df['nombre_cientifico'].isin(especies_seleccionadas)]
    #df_seleccion.boxplot('altura_arbol', by="nombre_cientifico")

    sns.pairplot(data = df_seleccion[cols_sel], hue = 'nombre_cientifico')

    plt.show()