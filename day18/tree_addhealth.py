# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:42:47 2019

@author: KIIT
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import numpy as np

df=pd.read_csv('tree_addhealth.csv')
df=df.replace(np.nan,df.mean())

features=df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values
labels=df.iloc[:,7:8].values

for i in range (0,13):
    if (i==6):
        continue
    onehotencoder=OneHotEncoder(categorical_features=[i])
    features=onehotencoder.fit_transform(features).toarray()
    features=features[:,1:]
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)
pred=classifier.predict(features_test)
result=pd.DataFrame(labels_test,pred)
print(result)
cm=list(confusion_matrix(labels_test,pred))
print(cm)
total=cm[0].sum()+cm[1].sum()
success=cm[0][0]+cm[1][1]
print('model success percent:',(success/total)*100)
    