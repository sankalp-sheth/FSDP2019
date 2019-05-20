# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:29:37 2019

@author: KIIT
"""

import numpy as np
import random
from collections import Counter
x=[]
for i in range (0,40):
    x.append(random.randint(5,15))
y=np.array(x)
c=Counter()
for num in y:
    c[num]+=1
t=dict(c)
