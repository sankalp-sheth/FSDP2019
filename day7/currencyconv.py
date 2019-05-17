# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:35:36 2019

@author: KIIT
"""

import requests
url="http://data.fixer.io/api/latest?access_key=5585e6d136bcc16619b7c4e2c966385c"
response=requests.get(url)
jsondata=response.json()
rate=float(jsondata["rates"]["INR"])
amount=float(input("Enter amount in EUR:"))
conv_amount=float(rate*amount)
print(conv_amount)

