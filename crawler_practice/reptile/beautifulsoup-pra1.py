from bs4 import BeautifulSoup
import lxml
from urllib.request import urlopen
html=urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# print(html)

soup = BeautifulSoup(html,"lxml")
print(soup.h1)
print(soup.p)
all_href=soup.find_all('a')
all_href=[l['href'] for l in all_href]
print('\n',all_href)