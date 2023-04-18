import pandas as pd #importa la librería Pandas, la cual permite trabajar con estructuras de datos llamadas dataframes en Python.


#carga un archivo CSV llamado "dataset_youtube.csv" en un dataframe llamado df.
df = pd.read_csv("dataset_youtube.csv")
print(df)
print(df.shape) #permite saber cuántas columnas y filas hay


#Guarda el nombre de las columnas del dataframe df en la variable nombre_columnas
#imprime cada nombre de columna en la consola
nombre_columnas = df.columns
for col in nombre_columnas:
    print(col)


#Para eliminar columnas
df.drop(["position","publishedAt","dislikeCount","channelId"], axis=1, inplace=True)
print(df.shape)


#Guarda los valores de la columna "channelTitle" del dataframe df en la variable canals e
# imprime los valores únicos de la columna "channelTitle" en la variable canals_unics.
canals = df["channelTitle"]
print(canals)

canals_unics = df.channelTitle.unique()
print(canals_unics)


#Crea dos dataframes nuevos, df_1 y df_2,
# que contienen las filas del dataframe original df donde el valor de la columna "channelTitle" es "NPR Music" y "KEXP",
# respectivamente. Imprime el número total de vídeos para cada canal en la consola.
df_1 = df.loc[df['channelTitle']=="NPR Music"]
df_2 = df.loc[df['channelTitle']=="KEXP"]

print(f"El canal NPR té un total de {df_1.shape[0]} videos")
print(f"El canal KEXP té un total de {df_2.shape[0]} videos")



#cCalcula el promedio de la columna "viewCount" para los dataframes df_1 y df_2,
# que corresponden a los canales "NPR Music" y "KEXP", respectivamente.
# Imprime los resultados en la consola.
print(f"El promig d'espectadors de NPR és de: {round(df_1['viewCount'].mean(),2)}") #el round sirve para redondear
print(f"El promig d'espectadors de KEXP és de: {round(df_2['viewCount'].mean(),2)}")


#calcula la diferencia absoluta sobre el promedio de espectadores del canal "df_2" y
# la cantidad de espectadores de cada video del canal "df_1".
prom_expectadors_1 = round(df_2['viewCount'].mean(),2)
prom_expectadors_2 = round(df_2['viewCount'].mean(),2)

for index, row in df_1.iterrows(): #per cada fila d'aquest datframe calculo el promig d'espectadors i s'afageix a una llista
    desviacio = prom_espectadors_1 - row['viewCount']
    list.desviacio.append(desviacio)

