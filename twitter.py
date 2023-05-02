import pandas as pd
import csv
import json
import glob

# Se obtienen todos los archivos JSON del directorio api_responses
files = glob.glob('api_responses/*.json')

# Se crea una lista vacía para almacenar los DataFrames individuales
llista_dfs = []

# Se crea una lista vacía para almacenar las tuplas de menciones
llista_de_tuplas = []

# Se itera sobre cada archivo JSON
for file in files:
    with open(file, encoding="utf-8") as jsonfile:
        dades = json.load(jsonfile)

        # Se obtienen todos los tweets del archivo JSON
        tweets = dades["data"]
        print(len(tweets))

        # Se itera sobre cada tweet
        for tweet in tweets:
            # Se extraen los campos relevantes del tweet
            text = tweet["text"]
            author_id = tweet["author_id"]
            users = dades["includes"]["users"]
            likes = tweet['public_metrics']['like_count']
            retweet = tweet['public_metrics']['retweet_count']
            created_at = tweet["created_at"]
            possibly_sensitive = tweet["possibly_sensitive"]
            retweet_count = tweet["public_metrics"]["retweet_count"]
            reply_count = tweet["public_metrics"]["reply_count"]
            like_count = tweet["public_metrics"]["like_count"]
            quote_count = tweet["public_metrics"]["quote_count"]
            impression_count = tweet["public_metrics"]["impression_count"]
            lang = tweet["lang"]
            hashtags = []

            # Obtiene el nombre de usuario y el número de seguidores del usuario que publicó el tweet
            for user in users:
                if user["id"] == author_id:
                    user_name = user["username"]
                    followers = user["public_metrics"]["followers_count"]
                    break

            # Extrae todas las menciones presentes en el tweet y las almacena como tuplas en una lista
            try:
                llista_mencions = tweet["entities"]["mentions"]
                for u in llista_mencions:
                    mencionat = u["username"]
                    tup = (user_name, mencionat, created_at)
                    llista_de_tuplas.append(tup)

            except KeyError:
                print("No hay menciones")
                pass

            # Se crea un DataFrame para el tweet
            df = pd.DataFrame({
                "user_id": [author_id],
                "user_name": [user_name],
                "followers": [followers],
                "text": [text],
                "lang": [lang],
                "created_at": [created_at],
                "impression_count": [impression_count],
                "retweet_count": [retweet_count],
                "reply_count": [reply_count],
                "quote_count": [quote_count],
                "hashtags": [hashtags],
            })

            # Se agrega el DataFrame a la lista de DataFrames individuales
            print(df)
            llista_dfs.append(df)


# Concatena todos los DataFrames individuales en un único DataFrame y se exporta a un archivo csv
df_final = pd.concat(llista_dfs)
df_final.to_csv("finaltableau.csv", sep=",")

# Crea un DataFrame con la lista de menciones y se exporta a un archivo csv
df_menciones = pd.DataFrame(llista_de_tuplas, columns=["source", "target", "created_at"])
df_menciones.to_csv("mention_gephi.csv", index=False)
