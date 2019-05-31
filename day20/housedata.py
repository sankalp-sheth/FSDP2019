# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:38:29 2019

@author: KIIT
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
df=pd.read_csv('kc_house_data.csv')
df['sqft_above']=df['sqft_above'].replace(np.nan,df['sqft_above'].mean())
def f(x):
    return int(x[0:4])
df['date']=df['date'].map(f)
features=df.drop('price',axis=1)
labels=df.iloc[:,2:3].values
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)
regressor=LinearRegression()
regressor.fit(features_train,labels_train) 
labels_pred = regressor.predict(features_test)   
print (np.mean(df.values[:,2:3]))
lasso = Lasso() 
ridge =  Ridge()
lasso.fit(features_train,labels_train)
ridge.fit(features_train,labels_train)
print('Linear Regression Mean Squared Error:',np.sqrt( metrics.mean_squared_error(labels_test, labels_pred))) 
print ("Lasso Regression Mean Square Error:",np.sqrt(metrics.mean_squared_error(labels_test,lasso.predict(features_test)))) 
print ("Ridge Regression Mean Square Error:",np.sqrt(metrics.mean_squared_error(labels_test,ridge.predict(features_test))))
print (np.mean(df.values[:,2:3]))
random=RandomForestRegressor(n_estimators=20,random_state=0)
random.fit(features_train,labels_train)
print('RandomForest Regression Mean Squared Error:',np.sqrt( metrics.mean_squared_error(labels_test, random.predict(features_test)))) 