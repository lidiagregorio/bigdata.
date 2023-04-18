variable='hola'
variable_2='adeu'

def losquesa(pip, cac):
    print(pip, cac)

losquesa(variable)


from twitchAPI.twitch import Twitch
import datetime #tiempo en que ha sido capturado
import pandas as pd #permite hacer el dataframes

now = datatime.datetime.now()

twitch = Twitch('o391ger2v3neggax02d30l2qa19xbw', 'cek72q8xasxrr68jusnc2afh0lapdz')

streams = twitch.get_streams(first=20, language='es', after='anira_variant') #función que baja los streams de twitch

dades = streams ["data"]

cursor = streams ['pagination']['cursor'] #para ir cogiendo los 100 seguidos

llista_dataframes = []

for dada in dades:
    captures_at = now
    user_id = data["user_id"]
    user_name = data["user_name "]
    game_id = data["game_id"]
    game_name = data["game_id"]
    title = data["title"]
    viwer_count = data["viwer_count "]
    started_at = data["started_at"]
    is_mature = data["is_mature"]

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

}, index=[0])
llista_dataframes.append(df)


final_dataframe = pd.concat(llista_dataframes) #te pone las dades de forma ordenada, como un excel
final_dataframe.to.csv ("export.csv", index=False)


