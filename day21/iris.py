# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:31:14 2019

@author: KIIT
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
df=pd.read_csv('Iris.csv')
features=df.iloc[:,1:-1].values
labels=df.iloc[:,-1].values
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
classifier=SVC(kernel='rbf',random_state=0)
classifier.fit(features_train,labels_train)
classifier.score(features_test,labels_test)
