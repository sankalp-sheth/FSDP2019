# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:21:35 2019

@author: KIIT
"""
import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce
import numpy as np
df=pd.read_csv('Telecom_churn.csv')
count=df.loc[(df['churn']==1) & (df['voice mail plan']=='yes') & (df['international plan']=='yes'),'churn'].count()
print(count)
churn=df[df['churn']==1]
intl_charge_churn=list(churn['total intl charge'])
non_churn=df[df['churn']==0]
intl_charge_non_churn=list(non_churn['total intl charge'])
sum1=reduce(lambda x,y:x+y,intl_charge_churn)
sum2=reduce(lambda x,y:x+y,intl_charge_non_churn)
list2=[sum1,sum2]
labels='churn','non churn'
colors=['blue','green']
plt.pie(list2,labels=labels, colors=colors, autopct='%1.4f%%', shadow=False, startangle=0)
plt.show()
total_night_minute=df[df['churn']==1]
night=np.array(total_night_minute['total night minutes'])
max1=night.max()
state=df[df['total night minutes']==max1]
print(state['state'])
intl_plan=churn.loc[churn['international plan']=='yes','international plan'].count()
local_plan=churn.loc[churn['voice mail plan']=='yes','voice mail plan'].count()
list5=[intl_plan,local_plan]
label1='international plan','voice mail plan'
plt.pie(list5,labels=label1, colors=colors, autopct='%1.4f%%', shadow=False, startangle=0)
plt.show()
churn_max_length=churn['account length'].max()
nonchurn_max_length=non_churn['account length'].max()
if churn_max_length>nonchurn_max_length:
    print('Max length customer:churn\nlength:',churn_max_length)
else:
    print('Max length customer:non churn\nlength:',nonchurn_max_length)
df['area code'][df['total intl calls']].value_counts().head(1)
churn['customer service calls'].value_counts()

