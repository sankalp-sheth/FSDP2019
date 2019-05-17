# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:41:57 2019

@author: KIIT
"""
import csv
l=[]
with open('population.csv','r') as fp:
    csv_reader = csv.reader(fp,delimiter = ',')
    for i in csv_reader:
        l.append(i)
def f_func(x):
    list