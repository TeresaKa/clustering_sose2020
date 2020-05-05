import requests
from bs4 import BeautifulSoup

URL = 'https://www.discogs.com/search/?q=abba&type=all'
html_doc = requests.get(URL)

soup = BeautifulSoup(html_doc.text, 'html.parser')
# print(soup.prettify())
header = soup.find_all('h3', class_='facets_header')
count = soup.find_all('small', class_='facet_count')
typ = soup.find_all('span', class_='facet_name')
for h in header:
    for c in h.children:
        print(c)

# for i in range(len(count)):
#     print("ghjklö", i)
#     print(count[i].string, typ[i].string)
