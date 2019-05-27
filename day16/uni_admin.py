# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:42:13 2019

@author: KIIT
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
df=pd.read_csv('University_data.csv')
features=df.iloc[:,:-1].values
labels=df.iloc[:,6]
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
regression=LinearRegression()
regression.fit(features_train,labels_train)
pred=regression.predict(features_test)
dataset=pd.DataFrame({'Actual':labels_test,'Prediction':pred})
print(dataset)
x=np.array([0,0,0,0,1,340,4.8,4.2,9.00,2])
x=x.reshape(1,-1)
predicted_chance=regression.predict(x)
print('Predicted chance:',predicted_chance)