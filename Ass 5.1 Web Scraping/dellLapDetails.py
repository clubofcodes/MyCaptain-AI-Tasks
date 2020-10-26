from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd

url = 'https://www.flipkart.com/search?q=dell+laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=dell+laptop%7CLaptops&requestId=5a7f282e-f4a4-4033-a58c-6fcd1d963d27&as-searchtext=de'
raw_html = requests.get(url)
data = BeautifulSoup(raw_html.content,'html5lib')

Dell_Laptop_info = data.find_all('div',attrs={'class':'_3wU53n'})
Dell_Laptop_price = data.find_all('div',attrs={'class':'_1vC4OE _2rQ-NK'})
lap_name = []
lap_price = []

for modelinfo in Dell_Laptop_info:
    # print(modelinfo.text)
    lap_name.append(modelinfo.text)

for modelprice in Dell_Laptop_price:
    # print(modelprice.text)
    lap_price.append(modelprice.text)

df_laptopModelprice = pd.DataFrame({'Mobile Name':lap_name,'Prices':lap_price})
df_laptopModelprice['Prices']=df_laptopModelprice.Prices.str.replace('₹','Rs.')
df_laptopModelprice.to_csv('dell.csv')