# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:22:00 2019

@author: KIIT
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
df=pd.read_csv('Foodtruck.csv')
features=df.iloc[:,:-1].values
labels=df.iloc[:,1].values
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
regression=LinearRegression()
regression.fit(features_train,labels_train)
pred=regression.predict(features_test)
dataset=pd.DataFrame({'Actual':labels_test,'Predicted':pred})
print(dataset)
plt.scatter(features,labels,color='Red')
plt.plot(features,regression.predict(features),color='Blue')
jaipur=np.array([3.073])
jaipur=jaipur.reshape(1,-1)
predict_jaipur=regression.predict(jaipur)
print('Profit in jaipur:',predict_jaipur)