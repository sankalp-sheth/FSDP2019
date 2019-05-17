# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:33:56 2019

@author: KIIT
"""
import re
expression=input("Enter expression:")
if re.search(r'^[+-]?[0-9]*\.[0-9]+',expression):
    print("Yes")
else:
    print("No")
    
    
    