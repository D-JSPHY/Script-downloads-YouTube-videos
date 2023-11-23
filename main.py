from pytube import YouTube
from pytube import Search

url_videos = []

#funcion que descarga los videos 
def descargar_video(link):
  BYT = YouTube(link)
  
  video = BYT.streams.get_highest_resolution()
  
  try:
    video = video.download()
  except:
    print("Error al descargar: " + str(video.title))
  #print(ve) 
  else:
    print(f"Descargado:{str(video.title)}")

#link = input("Link del video: ")
#descargar_video(link)

# Realiza la búsqueda en YouTube

from googleapiclient.discovery import build

api_key = 'Tus_credenciales'

# Crea un servicio de la API de YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

buscar = input("¿Que quieres buscar?: ")
numero_videos = input("¿Cuantos videos quieres descargar?: ")

# Realiza una búsqueda de videos con el término 'YouTube Rewind'
search_response = youtube.search().list(
    q=buscar,
    type='video',
    order='viewCount',
    part='id',
    maxResults=int(numero_videos)
).execute()

# Imprime las URL de los videos encontrados
for search_result in search_response.get('items', []):
    video_id = search_result['id']['videoId']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    url_videos.append(video_url)

contador = 1
for url_video in url_videos:
  objeto_YT = YouTube(url_video)
  print(f"{contador}){objeto_YT.title}\n{url_video}\n")
  contador += 1

respuesta = input("¿Quieres descargar los videos? (s/n): ")

if respuesta == "s":
  for url_video in url_videos:
    descargar_video(url_video)
  print("Videos descargados con éxito")
elif respuesta == "n":
  print("Okey, mira tus vídeos con internet")
else:
  print("Opcion invalida")
