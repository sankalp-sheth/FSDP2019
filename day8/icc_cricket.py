# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:05:24 2019

@author: KIIT
"""

from bs4 import BeautifulSoup
import requests
icc_ranking="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(icc_ranking).text
soup=BeautifulSoup(source,"lxml")
odi_table=soup.find('table',class_='table')
A=[]
B=[]
C=[]
D=[]
E=[]
for row in odi_table.findAll("tr"):
    country_info=row.findAll("td")
    if len(country_info)==5:
       A.append(country_info[0].text.strip())
       B.append(country_info[1].text.strip())
       C.append(country_info[2].text.strip())
       D.append(country_info[3].text.strip())
       E.append(country_info[4].text.strip())
import pandas as pd
from collections import OrderedDict
col_name=["Position","Team","Weighted Matches","Points","rating"]
col_data=OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data)
df.to_csv("odi_ranking")

icc_ranking="https://www.icc-cricket.com/rankings/mens/team-rankings/test"
source=requests.get(icc_ranking).text
soup=BeautifulSoup(source,"lxml")
test_table=soup.find('table',class_='table')
F=[]
G=[]
H=[]
I=[]
J=[]
for row in test_table.findAll("tr"):
    country_info=row.findAll("td")
    if len(country_info)==5:
       F.append(country_info[0].text.strip())
       G.append(country_info[1].text.strip())
       H.append(country_info[2].text.strip())
       I.append(country_info[3].text.strip())
       J.append(country_info[4].text.strip())
col_name=["Position","Team","Weighted Matches","Points","rating"]
col_data=OrderedDict(zip(col_name,[F,G,H,I,J]))
df = pd.DataFrame(col_data)
df.to_csv("test_ranking")

icc_ranking="https://www.icc-cricket.com/rankings/mens/team-rankings/t20i"
source=requests.get(icc_ranking).text
soup=BeautifulSoup(source,"lxml")
t20i_table=soup.find('table',class_='table')
K=[]
L=[]
M=[]
N=[]
O=[]
for row in t20i_table.findAll("tr"):
    country_info=row.findAll("td")
    if len(country_info)==5:
       K.append(country_info[0].text.strip())
       L.append(country_info[1].text.strip())
       M.append(country_info[2].text.strip())
       N.append(country_info[3].text.strip())
       O.append(country_info[4].text.strip())
col_name=["Position","Team","Weighted Matches","Points","rating"]
col_data=OrderedDict(zip(col_name,[K,L,M,N,O]))
df = pd.DataFrame(col_data)
df.to_csv("t20i_ranking")    