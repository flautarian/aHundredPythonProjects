import os
from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

html_request = requests.get(URL)

ycombinator_text = html_request.text

soup = BeautifulSoup(ycombinator_text, "html.parser")

all_movies = soup.findAll(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]

# print(movie_titles[::-1])

for n in range(len(movie_titles)-1, 0, -1):
    print (movie_titles[n])



