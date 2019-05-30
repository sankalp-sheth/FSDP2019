# -*- coding: utf-8 -*-
"""
Created on Fri May 31 01:24:21 2019

@author: KIIT
"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
df=pd.read_csv('tree_addhealth.csv')
df=df.replace(np.nan,df.mean())
features=df.iloc[:,[0,16]].values
labels=df.iloc[:,21:22].values
labelencoder=LabelEncoder()
features[:,1]=labelencoder.fit_transform(features[:,1])
onehotencoder=OneHotEncoder(categorical_features=[1])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
sc=StandardScaler()
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
features_train=sc.fit_transform(features_train)
features_test=sc.fit_transform(features_test)
classifier=DecisionTreeClassifier()
classifier.fit(features_train,labels_train)
cm=list(confusion_matrix(labels_test,classifier.predict(features_test)))
total=cm[0].sum()+cm[1].sum()
success=cm[0][0]+cm[1][1]
print('Decision tree model success percent:',(success/total)*100)
