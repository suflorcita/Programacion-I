import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 


if __name__ == '__main__':
    archivo_veredas = '../Data/arbolado-publico-lineal-2017-2018.csv'
    archivo_parques = "../Data/arbolado-en-espacios-verdes.csv"

    columnas_veredas = ['diametro_altura_pecho', 'altura_arbol']
    columnas_parques = ['diametro', 'altura_tot']
    nuevos_nombres = ['diametro_altura_pecho', 'altura']

    df_veredas = pd.read_csv(archivo_veredas, low_memory=False)
    df_parques = pd.read_csv(archivo_parques)

    # selecciono las filas con tipas y columnas especificadas
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][columnas_veredas].copy()
    df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][columnas_parques].copy()

    # renombro las columnas
    df_tipas_veredas = df_tipas_veredas.rename(columns={columnas_veredas[i]:nuevos_nombres[i] 
                                             for i in range(len(columnas_veredas))})
   
    df_tipas_parques = df_tipas_parques.rename(columns={columnas_parques[i]:nuevos_nombres[i] 
                                             for i in range(len(columnas_parques))})

    # agrego una columna con el ambiente
    df_tipas_veredas = df_tipas_veredas.assign(ambiente='vereda')
    df_tipas_parques = df_tipas_parques.assign(ambiente='parque')

    # junto ambos datasets
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

    # hago los boxplot
    df_tipas.boxplot('diametro_altura_pecho', by = "ambiente")
    df_tipas.boxplot('altura', by="ambiente")
    plt.show()