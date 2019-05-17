# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:05:39 2019

@author: KIIT
"""

from bs4 import BeautifulSoup
import requests
import sqlite3
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
data=requests.get(url).text
soup=BeautifulSoup(data,'lxml')
odi_table=soup.find("table",class_='table')
odi=[]
odi_p=[]
for row in odi_table.findAll("tr"):
    country=row.findAll("td")
    if len(country)==5:
        odi.append(country[1].text.strip())
        odi_p.append(country[0].text.strip())
conn=sqlite3.connect("cricket_ranking.db")
c=conn.cursor()
c.execute('create table odi(position integer,country varchar(20))')
r=len(odi)
for i in range(0,r):
    b="insert into odi values({},'{}')".format(odi_p[i],odi[i])
    c.execute(b)
c.execute("select*from odi")
c.fetchall()
conn.commit()
conn.close()