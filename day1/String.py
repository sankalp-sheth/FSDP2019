# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:04:54 2019

@author: KIIT
"""
name=input("Enter your string")
a=name.find(' ')
print(name[a+1:]+' '+name[0:a])

