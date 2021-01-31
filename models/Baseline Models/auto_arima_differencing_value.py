# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:41:43 2020

@author: Chethan
"""


import numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sb
import pmdarima as pm

# Importing Dataset
range1 = [i for i in range(1,11)]
ds =  pd.read_csv(r"C:/Users/Chethan/Downloads/preprocessed_dataset_final.csv", usecols = range1)

# Splitting the dataset into train & test subsets
n_obs = 140  # 20% test data
ds_train, ds_test = ds[:-n_obs], ds[-n_obs:]


max_diff = 0
for col in ds:
    diff = pm.arima.ndiffs(x= ds_train[col], test = 'adf', max_d = 4)
    if diff > max_diff:
        max_diff = diff
        
print(max_diff)