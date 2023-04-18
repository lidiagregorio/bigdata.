import pandas as pd
import numpy as np

#Carga el archivo CSV en un DataFrame (df) utilizando la función pd.read_csv()
df=pd.read_csv("/Users/Lidia/PycharmProjects/pythonProject2/EXCEL/feb_23_es_simple.csv", sep='\t')

#La primera línea obtiene el número de filas y la segunda el número de columnas del DataFrame
rows = df.shape[0]
cols = df.shape[1]

#Se imprime los nombres de las columnas del DataFrame, uno por uno, como una lista de las categorías o etiquetas de las columnas en el DataFrame.
print ('Las categorias de las columnas son:')
for col in df.columns:
    print (col)


#1.¿CUÁL HA SIDO LA EVOLUCIÓN DE ESPECTADORES (CAPTURA A CAPTURA) DURANTE EL PERIODO?

#Se crea un nuevo DataFrame llamado df1 que contiene únicamente las columnas 'captured_at' y 'viewer_count' del DataFrame original
df1 = df[['captured_at','viewer_count']]

#Se crea una lista llamada unique_list que contiene los valores únicos de la columna 'captured_at' del DataFrame df.
unique_list = list(df['captured_at'].unique())
print(unique_list)

#Se realiza un agrupamiento y suma en el DataFrame df basada en la columna 'captured_at', y el resultado se asigna a un nuevo DataFrame llamado df_sum.
#El .reset_index() sirve para resetear el índice del DataFrameGroupBy y convertirlo en un nuevo DataFrame con un índice numérico.
df_sum = df.groupby(['captured_at'])['viewer_count'].sum().reset_index()
print("La evolución de los espectadores durante el periodo ha sido:")
print(df_sum)
df_sum.to_csv('1.csv') #Exportamos el dataframe


#2.¿CUÁLES SON LAS CATEGORÍAS MÁS VISTAS Y EN LAS QUE MÁS HORAS DE DIRECTO SE HAN REALIZADO?

# Se convierte la columna 'captured_at' a tipo de dato datetime
df['captured_at'] = pd.to_datetime(df['captured_at'])

# Se calcula el total de visualizaciones por categoría
#El .agg() es una abreviatura de "aggregates" (agregaciones) y se utiliza para aplicar una o más operaciones a un DataFrame o a un objeto de tipo GroupBy.
categorias_vistas = df.groupby('game_name').agg({'viewer_count': 'sum'}).reset_index()

# Se ordena las categorías por el total de visualizaciones en orden descendente
categorias_vistas = categorias_vistas.sort_values(by='viewer_count', ascending=False)


# Se calcula el total de horas de directo por categoría
# Se calcula la diferencia en horas entre cada registro consecutivo en la columna 'captured_at' (esto es gracias al .diff()) y lo almacena en una nueva columna 'horas_directo' en el DataFrame df.
# El dt.total_seconds() se utiliza para convertir una cantidad de tiempo expresada en unidades de tiempo (como días, horas, minutos, etc.) a segundos.
# Por tanto, se divide los segundos entre 3600 (la cantidad de segundos en una hora) para obtener la diferencia en horas.
df['horas_directo'] = df['captured_at'].diff().dt.total_seconds() / 3600
categorias_horas = df.groupby('game_name').agg({'horas_directo': 'sum'}).reset_index()

# Se ordena las categorías por el total de horas de directo en orden descendente
categorias_horas = categorias_horas.sort_values(by='horas_directo', ascending=False)

# Se imprimir las 10 categorías con más visualizaciones. Esto se puede hacer por el .head(10).
print("Categorías con más visualizaciones:")
print(categorias_vistas.head(10))

# Se imprimir las 10 categorías con más horas de directo Esto se puede hacer por el .head(10).
print("Categorías con más horas de directo:")
print(categorias_horas.head(10))

categorias_vistas.to_csv('2.csv') #exportamos
categorias_horas.to_csv('3.csv') #exportamos


#3.¿CÓMO HAN EVOLUCIONADO (CAPTURA A CAPTURA) ESTAS CATEGORIAS A LO LARGO DEL MES?

# Se crea un nuevo DataFrame llamado df1 que contiene únicamente las columnas 'captured_at' y 'game_name' del DataFrame original
df1 = df[['captured_at', 'game_name']]

# Se crea una lista llamada unique_list que contiene los valores únicos de la columna 'captured_at' del DataFrame df1
unique_list = list(df1['captured_at'].unique())

# Se realiza un agrupamiento en el DataFrame df1 basado en las columnas 'captured_at' y 'game_name', y se imprime la evolución de las visualizaciones por categoría captura a captura
# Se utiliza el método value_counts() en la columna 'game_name' del DataFrame filtrado df_captured_at para obtener la cantidad de visualizaciones para cada categoría en esa captura.
print("La evolución de las visualizaciones por categoría durante el periodo ha sido:")
for captured_at in unique_list:
    df_captured_at = df1[df1['captured_at'] == captured_at]
    game_counts = df_captured_at['game_name'].value_counts()
    print(f"Captura: {captured_at}")
    print(game_counts)

game_counts.to_csv('4.csv') #exportamos


#4. ¿CUÁL ES LA DISTRIBUCIÓN DE LOS STREAMERS SI LOS CLASIFICAMOS POR VOLUMENES DE AUDIENCIA Y HORAS REALIZADAS?

# Se agrupa por 'streamer_name' y se calculaa la suma de 'viewer_count' y 'horas_directo' para cada streamer
streamers = df.groupby('streamer_name').agg({'viewer_count': 'sum', 'horas_directo': 'sum'}).reset_index()

# Se ordena los resultados por volumen de audiencia y horas realizadas de forma descendiente
streamers = streamers.sort_values(by=['viewer_count', 'horas_directo'], ascending=False)

# Se imprime la distribución de streamers por volumen de audiencia y horas realizadas
print("Distribución de streamers por volumen de audiencia y horas realizadas:")
print(streamers.head(10))

streamers.to_csv('4.csv', decimal=',') #exportamos

#5.¿CUÁL HA SIDO LA EVOLUCIÓN (CAPTURA A CAPTURA) DE LA DESVIACIÓN ESTÁNDAR EN EL VOLÚMEN DE ESPECTADORES?
# Se crea un nuevo DataFrame llamado df1 que contiene únicamente las columnas 'captured_at' y 'viewer_count' del DataFrame original
df1 = df[['captured_at','viewer_count']]

# Se agrupar por 'captured_at' y se calculaa la desviación estándar en el volumen de espectadores para cada captura con el .std()
df_std = df1.groupby('captured_at')['viewer_count'].std().reset_index()

# Se imprime la evolución captura a captura de la desviación estándar en el volumen de espectadores
print("La evolución de la desviación estándar en el volumen de espectadores durante el periodo ha sido:")
print(df_std)

df_std.to_csv('4.csv', index=False) #exportamos
