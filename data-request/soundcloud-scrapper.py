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


class Scrapper:
    def __init__(self, newOrTop="top", genre="all-music", country="US"):
        defaultURL = "https://soundcloud.com/charts/"
        self.currentURL = (
            defaultURL + newOrTop + "?genre=" + genre + "&country=" + country
        )

    def url_splitter(self):
        urlParams = self.currentURL.split("https://soundcloud.com/charts/")[1]
        chartType = urlParams.split("?")[0]
        genreCountry = urlParams.split("top?genre=")[1]
        genre = genreCountry.split("&")[0]
        restParams = genreCountry.split("&")[1]
        country = restParams.split("=")[1]
        return chartType, genre, country

    def songArtistPubCollection(self):
        chartType, genre, country = self.url_splitter()

        content = urllib.request.urlopen(self.currentURL).read()
        h2Tags = SoupStrainer("article")
        soupSongArtist = BeautifulSoup(
            content, "html.parser", parse_only=h2Tags
        ).select("h2 > a")

        song_url_list = []
        song_name_list = []
        artist_url_list = []
        artist_name_list = []
        publish_date_list = []

        i = 0
        for songArtist in soupSongArtist:
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

        timeTags = SoupStrainer("time")
        soupPubDate = BeautifulSoup(content, "html.parser", parse_only=timeTags)

        for pubDate in soupPubDate:
            publish_date_list.append(str(pubDate.text)[:10])

        print(publish_date_list)
