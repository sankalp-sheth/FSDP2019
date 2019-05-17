# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:59:46 2019

@author: KIIT
"""

import re
n=int(input("Please number of test cases"))
my_list=[]
my_list2=[]
for number in range (0,n):
    str=input()
    my_list.append(str)
for str1 in my_list:
    if re.match(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}$',str1):
        print("yes")
        my_list2.append(str1)
    else:
        print("no")
my_list2.sort()
print(my_list2)
        