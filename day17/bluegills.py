# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:41:45 2019

@author: KIIT
"""
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('bluegills.csv')
features=df.iloc[:,0:1].values
labels=df.iloc[:,1:].values
print('The relation is quadratic in nature.')
poly=PolynomialFeatures(degree=5)
poly_features=poly.fit_transform(features)
regression=LinearRegression()
regression.fit(poly_features,labels)
labels1=regression.predict(poly.transform(features))
plt.scatter(features,labels)
plt.plot(features,labels1)
x=5
x=np.array(x).reshape(1,-1)
pred=regression.predict(poly.transform(x))
print('Length of 5 year old fish:',pred)
