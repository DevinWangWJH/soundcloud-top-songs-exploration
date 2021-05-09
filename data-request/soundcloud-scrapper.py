import pandas as pd
import re
import datetime
import time

import requests
import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

        return song_name_list, artist_name_list, publish_date_list

    def songWeeklyAllTimeView(self):

        driver_path = "C:\Program Files (x86)\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=driver_path)
        browser.get(self.currentURL)

        weekly_view_list = []
        all_time_view_list = []

        last_height = browser.execute_script("return document.body.scrollHeight")

        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        weeklyPlaysPath = "//span[@class='sc-visuallyhidden']"

        weeklyAllTime = browser.find_elements_by_xpath(weeklyPlaysPath)[0:100]

        i = 0
        for element in weeklyAllTime:
            if i == 0:
                weekly_view_list.append(int(element.text))
                i += 1
            else:
                all_time_view_list.append(int(element.text))
                i -= 1

        return weekly_view_list, all_time_view_list
