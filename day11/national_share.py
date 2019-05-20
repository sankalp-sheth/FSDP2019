# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:48:10 2019

@author: KIIT
"""
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source=requests.get(url).text
soup=BeautifulSoup(source,"lxml")
right_table=soup.find('table',class_='wikitable')
national_share=[]
country=[]
count=0
for row in right_table.findAll('tr'):
    country_info=row.findAll('td')
    if len(country_info)==7:
        national_share.append(country_info[4].text.strip())
        country.append(country_info[1].text.strip())
        count+=1
    if count==6:
        break
explode=(0.1,0,0,0,0,0)
colors=['yellow','red','orange','green','blue','purple']
plt.pie(national_share, explode=explode, labels=country, colors=colors, autopct='%1.2f%%', shadow=True, startangle=90)
plt.show()
plt.savefig('nationalincome.jpg')