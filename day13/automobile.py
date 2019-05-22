# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:01:54 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Automobile.csv')
total_number=df['make'].value_counts()
explode=(0.1,0,0,0,0,0,0,0,0,0)
plt.pie(total_number.values[:10], explode=explode, labels=total_number.index[:10], autopct='%1.2f%%', shadow=True, startangle=0)