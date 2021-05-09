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
