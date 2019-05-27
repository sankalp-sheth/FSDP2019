# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:58:37 2019

@author: KIIT
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv('Bahubali2_vs_Dangal.csv')
features=df.iloc[:,0:1].values
labels_baahu=df.iloc[:,1].values
labels_dangal=df.iloc[:,2].values
features_train,features_test,labels_baahu_train,labels_baahu_test=train_test_split(features,labels_baahu,test_size=0.2,random_state=0)
regression=LinearRegression()
regression.fit(features_train,labels_baahu_train)
x=np.array([10])
x=x.reshape(1,-1)
predict_baahu=regression.predict(x)
print('10th day baahubali collections:',predict_baahu)
features_train,features_test,labels_dangal_train,labels_dangal_test=train_test_split(features,labels_dangal,test_size=0.2,random_state=0)
regress=LinearRegression()
regress.fit(features_train,labels_dangal_train)
y=np.array([10])
y=x.reshape(1,-1)
predict_dangal=regress.predict(y)
print('10th day Dangal collections:',predict_dangal)
