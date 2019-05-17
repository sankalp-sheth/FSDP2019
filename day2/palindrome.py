# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:46:47 2019

@author: KIIT
"""
number=[]
rev=0
f=0
n=int(input("Enter number of elements in list:"))
for n in range(0,n):
    num=int(input())
    number.append(num)
for num1 in number:
    num2=int(num1)
    print(num1)
    while(num1!=0):
        a=int(num1%10)
        rev=int(rev*10+a)
        num1=int(num1/10)
        print("{} ".format(rev))
    if rev==num2:
        rev=0
        continue
    else:
        f=1
        break
if f==1:
    print("false")
else:
    print("true")