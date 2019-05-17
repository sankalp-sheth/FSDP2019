# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:21:15 2019

@author: KIIT
"""

from pandas import DataFrame
import mysql.connector

conn=mysql.connector.connect(user='system_123',password='sankalp99',host='db4free.net',database='sankalp')
c=conn.cursor()
c.execute("create table students(name varchar(20),age integer,rollno integer,branch varchar(20));")
c.execute("insert into students values('Sankalp Sheth',20,1706356,'IT')")
c.execute("insert into students values('Rohan Wadhwa',20,1706350,'IT')")
c.execute("insert into students values('Ronit Ray',19,1706353,'CSE')")
c.execute("insert into students values('Riddhi Paliwal',21,1406256,'ECE')")
c.execute("insert into students values('Shreya Sanjay',22,2745352,'ETC')")
c.execute("insert into students values('Aayush Shekhar',18,1306256,'CSE')")
c.execute("insert into students values('Rishav Jain',21,1706356,'CIVIL')")
c.execute("insert into students values('Aastha Jain',18,1806426,'MECH')")
c.execute("insert into students values('Urvi Mehta',21,1816362,'IT')")
c.execute("insert into students values('Juhi Sheth',20,1736156,'ETC')")
c.execute("select*from students")
df=DataFrame(c.fetchall())
df.columns=['Name','Age','Roll_No','Branch']
conn.commit()
conn.close()