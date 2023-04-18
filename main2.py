from twitchAPI.twitch import Twitch  #importa la clase Twitch de la biblioteca twitchAPI.
import datetime #tiempo en que ha sido capturado. importa el módulo datetime que se utiliza para trabajar con fechas y tiempos en Python.
import pandas as pd #importa la biblioteca Pandas que se utiliza para trabajar con estructuras de datos llamadas DataFrames.
import time #importa el módulo time

now = datatime.datetime #guarda el objeto datetime en la variable now.

twitch = Twitch('o391ger2v3neggax02d30l2qa19xbw', 'cek72q8xasxrr68jusnc2afh0lapdz') #instancia la clase Twitch utilizando las credenciales de la API de Twitch.

llista_dataframes = [] #crea una lista vacía para almacenar los DataFrames creados posteriormente.
idiomes = ["es", "ca"] #define una lista de idiomas para filtrar los streams de Twitch.
cursor_dummy = None #define un valor inicial para la variable cursor_dummy.

def crida(cursor, lang): #define la función crida que acepta dos argumentos: cursor y lang.
    streams = twitch.get_streams(first=20, language='ca', after=cursor) #función que baja los streams de twitch
    dades = streams ["data"] #guarda los datos de la transmisión en la variable dades.

    for dada in dades: #El bucle for itera sobre cada transmisión en dades y extrae información específica de cada transmisió
        captures_at = now
        user_id = data["user_id"]
        user_name = data["user_name "]
        game_id = data["game_id"]
        game_name = data["game_id"]
        title = data["title"]
        viwer_count = data["viwer_count "]
        started_at = data["started_at"]
        is_mature = data["is_mature"]
        language = data ["lang"]

    df = pd.DataFrame({
            'captures_at':  captures_at,
            'user_id':  user_id,
            'user_name': user_name,
            'game_id': game_id,
            'game_name': game_name,
            'title': title,
            'viwer_count': viwer_count,
            'started_at': started_at,
            'is_mature': is_mature,
        'lang'

        }, index=[0]) #se utiliza para especificar el índice del DataFrame que se está creando, en este caso, se establece el índice como 0.
        llista_dataframes.append(df)

    print(len(llista_datframes))


    try:     #Indica que se va a intentar ejecutar el siguiente bloque de código.
        cursor = streams ['pagination']['cursor'] #se intenta obtener el cursor de paginación de la respuesta de la API de Twitch. Esto permitirá recuperar más datos en la próxima llamada a la API.
        print(f"Fent una nova consulta. Idioma: {lang} - Total de Stream "
              f"cursor)
        print ('dormint')
        time.sleep(1)
        crida(cursor, lang) #se llama recursivamente a la función crida con el nuevo cursor de paginación.

#indica que si se produce un error de tipo KeyError se va a ejecutar el siguiente bloque de código.
# Se muestra un mensaje en la consola indicando que se ha alcanzado la última página de resultados.
# Indica que no se va a hacer nada en caso de que se produzca el error KeyError.
    except KeyError:
        print('ultima pagina')
        pass


crida(cursor_dummy)

final_dataframe = pd.concat(llista_dataframes) #te pone las dades de forma ordenada, como un excel
final_dataframe.to.csv (f"export_´{lang}.csv", index=False)


