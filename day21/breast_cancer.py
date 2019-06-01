# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:44:58 2019

@author: SANKALP
"""
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
df=pd.read_csv('breast_cancer.csv')
val=list(df['G'].value_counts().head(1).index)
df['G']=df['G'].replace(np.nan,val[0])
features=df.iloc[:,1:-1].values
labels=df.iloc[:,-1].values
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
classifier=SVC(kernel='rbf',random_state=0)
classifier.fit(features_train,labels_train)
cm=list(confusion_matrix(labels_test,classifier.predict(features_test)))
print (cm)
total=cm[0].sum()+cm[1].sum()
success=cm[1][1]+cm[0][0]
print('success rate of model:',(success/total)*100)
predict=np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1)
if classifier.predict(predict)[0]==4:
    print('Cancer type is:Malignant Tumor')
else:
    print('Cancer type is:Benign Tumor')
gnb=GaussianNB()
gnb.fit(features_train,labels_train)
print("Gaussian NB",gnb.score(features_test,labels_test)*100)
bnb=BernoulliNB()
bnb.fit(features_train,labels_train)
print("BernoulliNB",bnb.score(features_test,labels_test)*100)
mnb=MultinomialNB()
mnb.fit(features_train,labels_train)
print("Multinomial NB:",mnb.score(features_test,labels_test)*100)