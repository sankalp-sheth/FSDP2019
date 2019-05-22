# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:51:44 2019

@author: KIIT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv')
df_job=df.groupby(['JobTitle','AnnualSalary'])
df_job.min()
df_job.max()
df_job.mean()
df_job.std()
aggregated=df_job.agg([np.min,np.max,np.std,np.mean])
df_sorted=aggregated.sort_values(by=['AnnualSalary'],ascending=[False])
df_sorted.head(1)
df_title=df.groupby(['JobTitle'])
print(df_title)
job_title=df['JobTitle'].value_counts().head(10)
len(job_title)
plt.pie(job_title.values,labels=job_title.index,startangle=0)
agency_id=[]
agency_name=[]
agency_id=list(df['AgencyID'].values)
agency_name=list(df['Agency'].values)
missing=df[df['GrossPay'].isnull()]