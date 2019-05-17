# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:21:52 2019

@author: KIIT
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
agent_list2=[]
def f(x):
    return random.choice(code_names)
agent_list=map(f,names)
print(list(agent_list))

agent_list2=[]
f=lambda x:random.choice(code_names)
for str1 in names:
    agent_list2.append(f(str1))
print(agent_list2)
