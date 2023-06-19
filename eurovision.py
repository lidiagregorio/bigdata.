import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

try:
    # Código de captura de excepción
    raise AttributeError("¡Esta es una excepción de prueba!")

except AttributeError as exc:
    print(f"Error: {exc}")

# Concatenar los dataframes en llista.dataframes
final = pd.concat(llista.dataframes)

# Guardar el dataframe concatenado en un archivo Excel
final.to_excel("llista_final.xlsx", index=False)

# Configuración de las credenciales de cliente de Spotify
SPOTIFY_CLIENT_ID = 'tu_client_id'
SPOTIFY_CLIENT_SECRET = 'tu_client_secret'

# Autenticación y acceso a la API de Spotify
auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# DataFrame de ejemplo
df = pd.DataFrame({
    "cantante": ["Artista 1", "Artista 2", "Artista 3"],
    "Canción": ["Canción 1»Versión 1", "Canción 2»Versión 2", "Canción 3»Versión 3"]
})

# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    artista = row["cantante"]
    track = row["Canción"].split("»")
    print(artista, track)


