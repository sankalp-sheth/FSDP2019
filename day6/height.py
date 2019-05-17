# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:40:28 2019

@author: KIIT
"""
from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
def f(x):
    if 'height' not in x:
        return False
    else:
        return True
filter_people=list(filter(f,people))
print(list(filter_people))
filter_height= list(map(lambda x:x['height'],filter_people))
print(list(filter_height))
total_height=reduce(lambda x,y: x+y,filter_height)
avg_height=total_height/len(filter_height)
print(avg_height)
