# -*- coding: utf-8 -*-
"""
Created on Fri May 31 01:44:46 2019

@author: KIIT
"""

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix
import numpy as np
from sklearn.ensemble import RandomForestClassifier
df=pd.read_csv('tree_addhealth.csv')
df=df.replace(np.nan,df.mean())

features=df.iloc[:,1:6].values
labels=df.iloc[:,7].values
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
classifier=RandomForestClassifier(n_estimators=25,random_state=0)
classifier.fit(features_train,labels_train)
cm=list(confusion_matrix(labels_test,classifier.predict(features_test)))
total=cm[0].sum()+cm[1].sum()
success=cm[0][0]+cm[1][1]
print('model success percent:',(success/total)*100)
