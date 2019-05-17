# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:42:50 2019

@author: KIIT
"""

names = ['Mary', 'Isla', 'Sam']
def f(x):
    return hash(x)
agent_list=map(f,names)
print(list(agent_list))
