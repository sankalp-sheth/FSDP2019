# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:53:26 2019

@author: KIIT
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import numpy as np
df=pd.read_csv('affairs.csv')

features=df.iloc[:,:-1].values
labels=df.iloc[:,8].values

onehotencoder1=OneHotEncoder(categorical_features=[6])
features=onehotencoder1.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder2=OneHotEncoder(categorical_features=[11])
features=onehotencoder2.fit_transform(features).toarray()
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
print('success rate of affair:',(success/total)*100)

random_women=np.array([3,25,3,1,4,16,4,2])
random_women=random_women.reshape(1,-1)
random_women=onehotencoder1.transform(random_women).toarray()
random_women=random_women[:,1:]
random_women=onehotencoder2.transform(random_women).toarray()
random_women=random_women[:,1:]
random_women=sc.transform(random_women)
print('Prediction:',classifier.predict(random_women))