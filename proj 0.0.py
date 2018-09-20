import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
from TextFromURL import TextFromURL
from Article import Article


url = "https://www.ynet.co.il/articles/0,7340,L-5341751,00.html#autoplay"
main_AT2 = Article(url)
main_AT2.create_file()
