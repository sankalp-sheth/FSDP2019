# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:40:46 2019

@author: KIIT
"""
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
df=pd.read_csv('http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat',delimiter=' ')
features=df.iloc[:,:-1].values
labels=df.iloc[:,8:].values
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)
regressor=LinearRegression()
regressor.fit(features_train,labels_train) 
labels_pred = regressor.predict(features_test)  
print (np.mean(df.values[:,-1]))
lasso = Lasso() 
ridge =  Ridge()
lasso.fit(features_train,labels_train)
ridge.fit(features_train,labels_train)
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print ("Lasso Regression Mean Square Error:",metrics.mean_squared_error(labels_test,lasso.predict(features_test))) 
print ("Ridge Regression Mean Square Error:",metrics.mean_squared_error(labels_test,ridge.predict(features_test)))
