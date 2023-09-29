from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy import *
import os

date = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= os.environ["SPOTIFY_CLIENTID"],
        client_secret= os.environ["SPOTIFY_SECRET"],
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]


for li in song_names_spans:
    li.contents[0] = str(li.contents[0]).replace("\t", "").replace("\n", "")
    print(li.contents)

song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)