import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.request import urlretrieve
searchName = input("Please enter your search term\n")
os.mkdir(searchName)
searchResults = list()
for i in range(1, 5):
    url = "http://[Redacted due to NDA]/page/" + str(i) + "?indexCatalogue=full-site-search&searchQuery=" + searchName + "[Redacted due to NDA]"

    r = requests.get(url)

    html = BeautifulSoup(r.content, features="html.parser")

    links = html.find("dl", class_="[Redacted due to NDA]")


    for link in links.find_all('a', href=True):
        if link['href'] not in searchResults:
            searchResults.append(link['href'])
    time.sleep(10)
print("Done retreiving all search results")

currentDirectory = os.path.dirname(os.path.abspath(__file__))
directory = (currentDirectory + "\\" + searchName + "\\")
for link in searchResults:
    link = link.strip()
    fileName = str(abs(hash(link[-36:]))) + link[-6:]
    saveTo = directory + fileName
    print(saveTo)
    urlretrieve(link, saveTo)
    time.sleep(10)
print("Done with everything")