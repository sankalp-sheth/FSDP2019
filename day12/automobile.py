# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:07:22 2019

@author: KIIT
"""

import pandas as pd
import numpy as np
df=pd.read_csv('Automobile.csv')
df['price']=df['price'].fillna(df['price'].mean())
list1=list(df['price'])
price=np.array(list1)
print('Minimum Price:',price.min())
print('Maximum Price:',price.max())
print('Average Price:',price.mean())
print('Standard Deviation:',price.std())
