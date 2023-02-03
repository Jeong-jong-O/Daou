import requests
from bs4 import BeautifulSoup

def tour_lst():
  response = requests.get('https://www.forbes.com/advisor/travel-rewards/top-50-best-places-to-visit/')
  soup = BeautifulSoup(response.content)
  soup_h2 = soup.find_all('h2')
  cnt = 0
  country = []
  for h2 in soup_h2:
    if 'Cards' not in h2.getText():
      print(h2.getText())
      country.append(h2.getText())
      cnt+=1
  print(cnt)
  return country


'''
response = requests.get('https://www.forbes.com/advisor/travel-rewards/top-50-best-places-to-visit/')
soup = BeautifulSoup(response.content, 'html.parser')
h2_tags = soup.findAll('h2',class_='')[1:]

for h2 in h2_tags:
   print(h2.get_text())
'''