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

urllink = "https://soundcloud.com/charts/top?genre=all-music&country=US"

driver_path = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)
browser.get(urllink)
# WebDriverWait(browser, 2).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.lazyLoadingList__list"))
# )

last_height = browser.execute_script("return document.body.scrollHeight")
print(last_height)

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# sourceData = browser.page_source
data = browser.find_elements_by_class_name("sc-visuallyhidden")[1:100]

for element in data:
    print(element.text)

browser.quit()

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
