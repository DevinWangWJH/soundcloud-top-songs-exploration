from bs4 import BeautifulSoup
import requests

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

for genre in genres:
    url = "https://soundcloud.com/charts/top?genre=" + genre + "&country=US"
    print(url)

# r = requests.get(urllink)
# soup = BeautifulSoup(r.text, "html.parser")


# print(soup.prettify())
