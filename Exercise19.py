from bs4 import BeautifulSoup
import requests

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
articles = soup.find_all('p')

for article in articles:
    print(article.text)