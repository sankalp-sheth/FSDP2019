# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:52:54 2019

@author: KIIT
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
df=pd.read_csv('mushrooms.csv')
features=df.iloc[:,[5,21,22]].values
labels=df.iloc[:,0:1].values

labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])
features[:,1]=labelencoder.fit_transform(features[:,1])
features[:,2]=labelencoder.fit_transform(features[:,2])
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder=OneHotEncoder(categorical_features=[1])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder=OneHotEncoder(categorical_features=[2])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
labels[:,0]=labelencoder.fit_transform(labels[:,0])
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
"""sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test) """
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)
pred=classifier.predict(features_test)
result=pd.DataFrame(labels_test,pred)
print(result)
cm=list(confusion_matrix(labels_test,pred))
total=cm[0].sum()+cm[1].sum()
success=cm[0][0]+cm[1][1]
print('success rate:',(success/total)*100)