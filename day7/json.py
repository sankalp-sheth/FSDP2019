# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:47:23 2019

@author: KIIT
"""

import requests
import time
url1="http://api.openweathermap.org/data/2.5/weather"
url2="?q="+input("Please enter City:")
url3="&appid=e9185b28e9969fb7a300801eb026de9c"
url=url1+url2+url3
response=requests.get(url)
response.content
jsondata=response.json()
print("Latitude:")
print(jsondata["coord"]["lat"])
print("Longitude:")
print(jsondata["coord"]["lon"])
print("Weather condition:")
print(jsondata["weather"][0]["main"])
print("Weather Speed:")
print(jsondata["wind"]["speed"])
print("Sunset timing:")
list1=list(time.localtime(jsondata["sys"]["sunset"]))
print("{}:{}:{}".format(list1[3],list1[4],list1[5]))
print("Sunrise timing:")
list2=list(time.localtime(jsondata["sys"]["sunrise"]))
print("{}:{}:{}".format(list2[3],list2[4],list2[5]))