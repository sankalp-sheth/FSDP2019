# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:59:42 2019

@author: KIIT
"""

my_list=input("Enter number sequence to be checked:").split(",")
my_list2=[]
for i in my_list:
    if int(i)>0:
        rev=i[::-1]
    if rev==i:
        my_list2.append(True)
    else:
        my_list2.append(False)  
print(any(my_list2))
        
        