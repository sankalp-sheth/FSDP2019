# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:13:41 2019

@author: KIIT
"""

import numpy as np
import matplotlib.pyplot as plt

data=np.random.normal(150,20,1000)
plt.hist(data,100)
print("Variance:")
print(data.var())
print("Standard Deviation:")
print(data.var()**2)