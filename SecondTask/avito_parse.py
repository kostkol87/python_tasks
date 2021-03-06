# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen
import sys


# url = sys.argv[1]
url = 'https://www.avito.ru/sankt-peterburg/kvartiry/2-k_kvartira_53_m_15_et._443405288'
html_doc = urlopen(url).read()
soup = BeautifulSoup(html_doc)


# id
id = url[-9:]
print id

# title
titleTag = soup.html.head.title
title = titleTag.string
print title

#city
city = (soup.find('div', id='map')).string
print city

# address
met=''
addr = soup.find('span', itemprop="streetAddress")
print addr.string
metro = str(addr.find_parent())
i=6
while(metro[i] !=','):
    met += metro[i]
    i += 1
print met

#content
description=''
cont = soup.find('div', id='desc_text')
for descr in cont:
    description += descr.string
print description

# price
scripts = str(soup.find_all('script'))
price_inx = str(scripts).find('par_price')
price = ''
while (scripts[price_inx+13] != '"'):
    price += scripts[price_inx+13]
    price_inx += 1
print price

