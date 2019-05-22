# -*- coding: utf-8 -*-
"""
Created on Thu May 23 01:57:56 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('ign.csv')
games=df['title'][(df['score']>7)&(df['platform']=='Xbox One')]
print(games)
ps4=df['score'][df['platform']=='PlayStation 4']
xbox=df['score'][df['platform']=='Xbox One']
plt.hist(ps4,bins=10)
plt.hist(xbox,bins=10)
