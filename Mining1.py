import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
searchName = input("Please enter your search term\n")
os.mkdir(searchName)
searchResults = list()
for i in range(1, 100):
    url = "http://[Redacted due to NDA]/search?query=" + searchName + "&page=" + str(i)

    r = requests.get(url)

    html = BeautifulSoup(r.content, features="html.parser")

    links = html.find("table", id="search-results")

    for link in links.find_all('a', href=True):
        searchResults.append("http://[Redacted due to NDA]" + link['href'])
print("Done retreiving all search results")
#Filter to search results with files attached
filteredResults = list()
previousline = ""
for line in searchResults:
    if line == previousline:
        filteredResults.append(line)
    previousline = line
print("Done filtering results to those with documents attached")

docURLs = list()
for line in filteredResults:
    line = line.strip()
    r = requests.get(line)

    html = BeautifulSoup(r.content, features="html.parser")

    links = html.find("div", id="item-images")

    for link in links.find_all('a', href=True):
        docURLs.append(link['href'])
        # write.write(link['href'] + "\n")
        # print(link['href']
print("Done getting the document URLs")
currentDirectory = os.path.dirname(os.path.abspath(__file__))
directory = (currentDirectory + "\\" + searchName + "\\")
for link in docURLs:
    link = link.strip()
    fileName = link[-36:]
    saveTo = directory + fileName
    urlretrieve(link, saveTo)
print("Done with everything")