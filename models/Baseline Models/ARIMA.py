# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 23:26:25 2020

@author: Chethan
"""

import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
import matplotlib.pyplot as plt
import glob

path = r'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/Research Project/DataSet/' # use your path
all_files = glob.glob(path + "/*.csv")

li = [] 
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

df2  = li.iloc[:, 0:2]

df2 = df2.astype({"YSSY_LOWW": float, "KLAX_EDDF": float})
df2.info()
df2.head()


# Augmented Dickey-Fuller Test (ADF Test)/unit root test
from statsmodels.tsa.stattools import adfuller
def adf_test(ts, signif=0.05):
    dftest = adfuller(ts, autolag='AIC')
    adf = pd.Series(dftest[0:4], index=['Test Statistic','p-value','# Lags','# Observations'])
    for key,value in dftest[4].items():
       adf['Critical Value (%s)'%key] = value
    print (adf)
    
    p = adf['p-value']
    if p <= signif:
        print(f" Series is Stationary")
    else:
        print(f" Series is Non-Stationary")
#apply adf test on the series
adf_test(df2["KLAX_EDDF"])

# 1st difference
df_differenced = df2.diff().dropna()
adf_test(df_differenced["KLAX_EDDF"])

#df_differenced2 = df_differenced.diff().dropna()
#adf_test(df_differenced2["KLAX_EDDF"].astype(float))

# model fitting
model = VAR(df_differenced)
results = model.fit(maxlags=15, ic='aic')
results.summary()