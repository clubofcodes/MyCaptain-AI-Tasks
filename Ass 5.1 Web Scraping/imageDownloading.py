from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd
from os.path import basename

url = 'https://www.passiton.com/inspirational-quotes'
raw_html = requests.get(url)
data = BeautifulSoup(raw_html.content,'html5lib')

all_quotes = data.find('div',attrs={'id':'all_quotes'})
links=[]

for quote in all_quotes.find_all('div',attrs={'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    links.append(quote.img['src'].split('?')[0])

for link in links:
    with open(f'F:\\Uni\\RKU\\5th SEM\Python Programming II - CE523\ASS Py Files\Ass 5.1\images\{basename(link)}','wb') as file:
        if(file.write(requests.get(link).content)):
            print(basename(link)," Downloaded...")