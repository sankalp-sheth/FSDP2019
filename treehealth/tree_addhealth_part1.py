# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:37:50 2019

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
features=df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values
labels=df.iloc[:,7:8].values
labelencoder=LabelEncoder()
features[:,8]=labelencoder.fit_transform(features[:,8])
onehotencoder=OneHotEncoder(categorical_features=[8])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)
classifier=DecisionTreeClassifier()
classifier.fit(features_train,labels_train)
cm=list(confusion_matrix(labels_test,classifier.predict(features_test)))
total=cm[0].sum()+cm[1].sum()
success=cm[0][0]+cm[1][1]
print('Decision tree model success percent:',(success/total)*100)
random=RandomForestClassifier(n_estimators=20,random_state=0)
random.fit(features_train,labels_train)
cm=list(confusion_matrix(labels_test,random.predict(features_test)))
total=cm[0].sum()+cm[1].sum()
success=cm[0][0]+cm[1][1]
print('Random Tree model success percent:',(success/total)*100)
