# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:34:25 2019

@author: KIIT
"""

import pandas as pd
import numpy as np
from apyori import apriori
df=pd.read_csv('Market_Basket_Optimisation.csv',header=None)
df=df.replace(np.nan,'none')
transactions=[]
temp=[]
type(df.values[1,3])
for i in range(0,7501):
    for j in range (0,20):
        if df.values[i,j]=='none':
            continue
        else:
            temp.append(df.values[i,j])
    transactions.append(temp)
    temp=[]
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)
results = list(rules)
for item in results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")