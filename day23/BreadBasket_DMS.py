# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:36:22 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori
import numpy as np
df=pd.read_csv('BreadBasket_DMS.csv')
df['Item']=df['Item'].replace('NONE',np.nan)
labels=list(df['Item'].value_counts().head(15).index)
sizes=list(df['Item'].value_counts().head(15).values)
df=df.dropna()
plt.pie(sizes,labels=labels)
plt.show()
transaction=[]
temp=[]
df_tr=pd.DataFrame()
for i in range(1,9685):
    df_tr=df[df['Transaction']==i]
    for j in df_tr['Item']:
        temp.append(j)
    transaction.append(temp)
    temp=[]
rules=apriori(transaction,min_support=0.0025,min_confidence=0.2,min_lift=3)
results=list(rules)
for item in results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
