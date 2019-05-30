# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:29:30 2019

@author: KIIT
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import numpy as np
df=pd.read_csv('PastHires.csv')
features=df.iloc[:,:-1].values
labels=df.iloc[:,6].values
labelencoder1=LabelEncoder()
features[:,1]=labelencoder1.fit_transform(features[:,1])
labelencoder2=LabelEncoder()
features[:,3]=labelencoder2.fit_transform(features[:,3])
labelencoder3=LabelEncoder()
features[:,4]=labelencoder3.fit_transform(features[:,4])
labelencoder4=LabelEncoder()
features[:,5]=labelencoder4.fit_transform(features[:,5])
onehotencoder=OneHotEncoder(categorical_features=[3])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test=sc.transform(features_test)
classifier=DecisionTreeClassifier()
classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_test)
result=pd.DataFrame(labels_test,labels_pred)
print(result)
cm=list(confusion_matrix(labels_test,labels_pred))
print(cm)
total=cm[0].sum()+cm[1].sum()
success=cm[1][1]
print('success rate for being hired:',(success/total)*100)
regress=RandomForestClassifier(n_estimators=25, random_state=0)
regress.fit(features_train,labels_train)
predict1=np.array([10,'Y',4,'BS','Y','N']).reshape(1,-1)
predict2=np.array([10,'N',4,'MS','N','Y']).reshape(1,-1)
predict1[:,1]=labelencoder1.transform(predict1[:,1])
predict1[:,3]=labelencoder2.transform(predict1[:,3])
predict1[:,4]=labelencoder3.transform(predict1[:,4])
predict1[:,5]=labelencoder4.transform(predict1[:,5])
predict1=onehotencoder.transform(predict1).toarray()
predict1=predict1[:,1:]
predict2[:,1]=labelencoder1.transform(predict2[:,1])
predict2[:,3]=labelencoder2.transform(predict2[:,3])
predict2[:,4]=labelencoder3.transform(predict2[:,4])
predict2[:,5]=labelencoder4.transform(predict2[:,5])
predict2=onehotencoder.transform(predict2).toarray()
predict2=predict2[:,1:]
sc.transform(predict1)
sc.transform(predict2)
print("Employment chances of candidate 1:",regress.predict(predict1))
print("Employment chances of candidate 2:",regress.predict(predict2))