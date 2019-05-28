# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:40:56 2019

@author: KIIT
"""
import numpy as np
import statsmodels.api as sm
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df=pd.read_csv('Female_Stats.csv')
features=df.iloc[:,1:].values
features_momheight=df.iloc[:,1:2].values
features_dadheight=df.iloc[:,2:].values
labels=df.iloc[:,0].values
features=sm.add_constant(features)
features_opt=features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
print("Both heights are equally important in predicting child's height.")
array2=np.array(labels)
print('Average height before:',array2.mean())
momheight=features_momheight+1
features_train,features_test,labels_train,labels_test=train_test_split(momheight,labels,test_size=0.2,random_state=0)
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
array1=np.array(regressor.predict(momheight))
print('After increasing mom height by 1:',array1.mean())
diff=array1.mean()-array2.mean()
print('Height increased:',diff)
dadheight=features_dadheight+1
features_train,features_test,labels_train,labels_test=train_test_split(dadheight,labels,test_size=0.2,random_state=0)
regress1=LinearRegression()
regress1.fit(features_train,labels_train)
array3=np.array(regress1.predict(dadheight))
print('After increasing dad height by 1:',array3.mean())
diff=array3.mean()-array2.mean()
print('Height increased:',diff)