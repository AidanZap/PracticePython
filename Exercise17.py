#Exercise17
    #Grab article titles from the New York Times using requests and Beautiful Soup

import requests
from bs4 import BeautifulSoup

def findTitles(url):

    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    headlines = soup.find_all('h2')

    for headline in headlines:
        headline = headline.text
        print(headline)

findTitles('http://nytimes.com')