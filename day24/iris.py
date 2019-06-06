# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:08:34 2019

@author: KIIT
"""

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df=pd.read_csv('Iris.csv')
features=df.iloc[:,[1,2,3,4]].values
pca=PCA(n_components=2)
features=pca.fit_transform(features)
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Iris-Setosa')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Iris-versicolor')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Iris-virginica')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('P1 Features')
plt.ylabel('P2 Features')
plt.legend()
plt.show()

