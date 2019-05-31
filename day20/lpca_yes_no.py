# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:27:02 2019

@author: KIIT
"""

from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
df=pd.read_csv('http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat',delimiter=' ')
def f(x):
    if x<df['lpsa'].mean():
        return 'Yes'
    else:
        return 'No'
df['lpsa']=df['lpsa'].map(f)
features=df.iloc[:,:-1].values
labels=df.iloc[:,8:].values
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)
regress=LogisticRegression()
regress.fit(features_train,labels_train)
result=pd.DataFrame(labels_test,regress.predict(features_test))
print(result)
cm=confusion_matrix(labels_test,regress.predict(features_test))
print (cm) 