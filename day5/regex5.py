# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:25:47 2019

@author: KIIT
"""
import re
with open("simpsons_phone_book.txt","r") as fp:
    s=fp.readlines()
for i in s:
    if re.match(r'^J.*Neu',i):
        print(i)