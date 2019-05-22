# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:58:36 2019

@author: KIIT
"""

import pandas as pd

df=pd.read_csv('training_titanic.csv')
survived=df.loc[(df['Survived']==1),'Survived'].count()
print('Survived:',survived)
died=df.loc[(df['Survived']==0),'Survived'].count()
print('Died:',died)
list1=list(df['Survived'].value_counts(normalize=True)*100)
print('Died %:',list1[0])
print('Survived %:',list1[1])
male=df[(df['Sex']=='male')]
female=df[(df['Sex']=='female')]
list2=list(male['Survived'].value_counts(normalize=True)*100)
list3=list(female['Survived'].value_counts(normalize=True)*100)
print('Male survival Rate:',list2[1])
print('Female survival Rate:',list3[1])
df['Child']=df['Age'].map(lambda x: 1 if x<18 else 0)
child=df[(df['Child']==1)]
list4=list(child['Survived'].value_counts(normalize=True)*100)
print('Child survival Rate:',list4[1])