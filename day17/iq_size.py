# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:18:31 2019

@author: KIIT
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
df=pd.read_csv('iq_size.csv')
features=df.iloc[:,1:].values
labels=df.iloc[:,0:1].values
regression=LinearRegression()
regression.fit(features,labels)
values=np.array([90,70,150])
values=values.reshape(1,-1)
pred=regression.predict(values)
print('IQ:',pred) #for brain=90,height=70,weight=150
features=sm.add_constant(features)
features_opt=features[:,[0,1,2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
print('Pvalue of brain size:',regressor_OLS.pvalues.min()) #seen by regressor_OLS.summary()
print('Intellegence is most dependent on brain size.')
