# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:13:02 2019

@author: KIIT
"""
number=[]
f=0
n=int(input("Enter number of numbers in list:"))
for n in range (0,n):
    num=input()
    number.append(num)
for str1 in number:
    rev=str1[::-1]
    if str1==rev:
        print("true")
        break
    else:
        f=1
        continue
if f==1:
    print("false")
    
        
        