import requests
from bs4 import BeautifulSoup

def python_crawling():
    response = requests.get('https://en.wikipedia.org/wiki/Python')
    soup = BeautifulSoup(response.content, 'html.parser')

    li_tags = soup.find_all('li', 'toclevel-1')

    for li in li_tags:
        print(li.get_text()[2:])