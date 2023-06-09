import pandas as pd #importa la librería Pandas, la cual permite trabajar con estructuras de datos llamadas dataframes en Python.
import time #importa la librería time.

#Lee un archivo de datos en formato CSV llamado "feb-full-2023.csv"
# y guarda solo algunas de sus columnas en un DataFrame llamado "df".
inici = time.time()

df=pd.read_csv("feb-full-2023.csv",
               sep='\t',
               usecols["captured_at","streamer_name","viwer_count","game_name","strem_title",])#el usecols sirve para sbaer que parámetros quieres
                chunksize=1000 #converitrá el dataframe en una especie de lista de 1000 registros
print(df)


#Selecciona solo los datos del streamer "kingdleague" y los guarda en "dades_kings_leage"

llista_kings_leage = []
for chunk in df:  #Se itera a través del dataframe df en bloques definidos por el parámetro chunksize que se usó al leer el archivo csv.
    dades_kings_leage = chunk[chunk["streamer_name"] == "kingdleague"] #Se seleccionan los datos del streamer "kingdleague" dentro del bloque actual (chunk) y se almacenan en la variable dades_kings_leage.

    llista_kings_leage.append(dades_kings_leage) #Se agregan los datos del streamer "kingdleague" del bloque actual a la lista llista_kings_leage.

#Se concatenan los datos de todos los bloques en la lista llista_kings_leage en un solo dataframe llamado final_frame.
#Se guarda el dataframe final_frame en un archivo csv llamado "kingsleague.csv"
# sin incluir la columna de índices (index=False).
final_frame = pd.concat(llista_kings_league)
final_frame.to_csv("kingsleague.csv", index=False)


#utiliza la función glob del módulo glob para buscar todos los archivos que terminen en ".csv"
# en el directorio actual y devuelve una lista con los nombres de los archivos encontrados.
llista_de_datasets = glob.glob("*.csv")
print(llista_de_datasets)=



#para saber que stream es el más visto
posicio = df["viewer_count"].idmax() #busca el índice de la fila con el valor máximo en la columna "viewer_count" del dataframe df y lo guarda en la variable posicio.

#imprime la información del stream con más espectadores, utilizando los valores de las columnas "captured_at",
# "streamer_name", "streamer_title" y "viewer_count" en la fila correspondiente al índice posicio.
print(df["captured_at"].iloc[posicio],["streamer_name"].iloc[posicio],df["streamer_title"].iloc[posicio], df["viewer_count"].iloc[posicio])

#crea un nuevo dataframe llamado dades_kings_leage que contiene todas las filas de df
# donde el valor en la columna "streamer_name" es igual a "kingleague".
dades_kings_leage = df[df["streamer_name"] == "kingleague"]

print(dades_kings_leage)

dades_kings_leage.to.csv("kingsleague.csv", index=False)




sample = df.sample(frac=0.1) #el 0.1 es un 10% del dataset

print(sample)

final = time.time()

print(final-inici)


list = []
df=pd.read_csv("/Users/Lidia/PycharmProjects/pythonProject2/EXCEL/feb_23_es_simple.csv", chunksize=10000, sep='\t', usecols=["captured_at","viewer_count"])

for chunk in df:
    df2 = df.groupby(['captured_at'])['viewer_count'].sum().reset_index()
    list.append(df2)
    print (chunk)

final_frame_1 = pd.contact(list)
final_frame_2 = final_frame_1.groupby("captured_at")["viewer_count"]reset_index()
final_frame_2.to_csv("test_2.csv")


df2_sum = df.groupby(['game_name'])['viewer_count'].sum().reset_index()

print(df2_sum)
