# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:09:41 2019

@author: KIIT
"""
from functools import reduce
my_list=input("Enter sequence of numbers:").split(",")
def f_func(x):
    if x%2==1:
        return True
    else:
        return False
print(my_list)
def m_func(x):
    return int(x)
def r_func(x,y):
    return x*y
def productofodds(list1):
    return reduce(r_func, filter(f_func, map(m_func, my_list)))
print(productofodds(my_list))
