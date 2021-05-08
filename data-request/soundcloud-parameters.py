from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import urllib.request
import os
import pandas as pd
import re
import datetime
from selenium import webdriver
import time

urllink = "https://soundcloud.com/charts/top?genre=all-music&country=US"

# driver_path = "C:\Program Files (x86)\chromedriver.exe"
# browser = webdriver.Chrome(executable_path=driver_path)
# browser.get(urllink)


def url_splitter(url):
    urlParams = url.split("https://soundcloud.com/charts/")[1]
    chartType = urlParams.split("?")[0]
    genreCountry = urlParams.split("top?genre=")[1]
    genre = genreCountry.split("&")[0]
    restParams = genreCountry.split("&")[1]
    country = restParams.split("=")[1]
    return chartType, genre, country


content = urllib.request.urlopen(urllink).read()
h2Tags = SoupStrainer("article")
soup = BeautifulSoup(content, "html.parser", parse_only=h2Tags).select("h2 > a")
song_url_list = []
song_name_list = []
artist_url_list = []
artist_name_list = []
i = 0
for songArtist in soup:
    if i == 0:
        column_name = "song"
        song_url_list.append(str(songArtist.get("herf", "/")))
        song_name_list.append(str(songArtist.text))
        i += 1
    else:
        column_name = "artist"
        artist_url_list.append(str(songArtist.get("href", "/")))
        artist_name_list.append(str(songArtist.text))
        i -= 1

print(song_name_list, artist_name_list)

genres = [
    "alternativerock",
    "ambient",
    "classical",
    "country",
    "danceedm",
    "dancehall",
    "deephouse",
    "disco",
    "drumbass",
    "dubstep",
    "electronic",
    "folksingersongwriter",
    "hiphoprap",
    "house",
    "indie",
    "jazzblues",
    "latin",
    "metal",
    "piano",
    "pop",
    "rbsoul",
    "reggae",
    "reggaeton",
    "rock",
    "soundtrack",
    "techno",
    "trance",
    "trap",
    "triphop",
    "world",
]
