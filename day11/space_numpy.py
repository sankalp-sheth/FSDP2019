# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:08:46 2019

@author: KIIT
"""
import numpy as np
numbers=input('enter numbers:').split(',')
def f(x):
    return int(x)
num_int=list(map(f,numbers))
x=np.array(num_int)
x=x.reshape(3,3)
print(x)