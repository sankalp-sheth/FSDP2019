# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:47:07 2019

@author: KIIT
"""
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
df=pd.read_csv('Auto_mpg.txt',header=None,delimiter=r'\s+')
columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
df.columns=columns
name=df['car name'][df['mpg']==df['mpg'].max()]
print('Car with highest mpg value:',name.values[0])
value=df['horsepower'].value_counts().head(1)
v=list(value.index)
df['horsepower']=df['horsepower'].replace('?',v[0])
features=df.iloc[:,1:8].values
labels=df.iloc[:,0:1].values
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
regressor=DecisionTreeRegressor()
regressor.fit(features_train,labels_train)
print('success rate:',regressor.score(features_test,labels_test)*100)
regress=RandomForestRegressor(n_estimators=25,random_state=0)
regress.fit(features_train,labels_train)
print('success rate:',regress.score(features_test,labels_test)*100)
predict=np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)
print('MPG Value by RandomForest:',regress.predict(predict))
print('MPG Value by DecisionTree:',regressor.predict(predict))