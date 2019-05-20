# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:30:21 2019

@author: KIIT
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
plt.hist(incomes,50)
print('Mean:',np.mean(incomes))
print('Median:',np.median(incomes))
incomes=np.append(incomes,100000)