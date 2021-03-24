#!/usr/bin/python3

'''
  Requirements:
    - ubuntu 21.04
    - apt -y install python3-bs4 python3-html5lib python3-requests
'''
import bs4
import re
import requests
import unicodedata

u = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"
#u = "https://en.wikipedia.org/wiki/Linux"
b = bs4.BeautifulSoup(requests.get(u).text, features="html5lib")

for x in b.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    level = int(re.search(r'h([0-9]+)', x.name, re.I).group(1))
    text = re.sub(r'\s+', ' ', x.get_text())
    text = re.sub(r'(^ +| +$)', '', text)
    print(' ' * (level - 1) + '* ' + unicodedata.normalize('NFKC', text))
    continue

