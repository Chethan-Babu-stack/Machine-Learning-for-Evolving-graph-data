# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:10:25 2020

@author: Chethan
"""

import numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sb
import pmdarima as pm

# Importing Dataset
range1 = [i for i in range(0,3)]
df =  pd.read_csv(r"C:/Users/Chethan/Downloads/preprocessed_dataset.csv", usecols = range1)
ds = df.drop(['day'], axis = 1)




def iterate(name, ds, col_number):
    # Splitting the dataset into train & test subsets
    n_obs = 100  # 20% test data
    ds_train, ds_test = ds[:-n_obs], ds[-n_obs:]
    
    # fitting a stepwise model:
    stepwise_fit = pm.auto_arima(ds_train, start_p=1, start_q=1, max_p=3, max_q=3, m=12,
                                 start_P=0, seasonal=True, d=1, D=1, trace=True,
                                 error_action='ignore',  # don't want to know if an order does not work
                                 suppress_warnings=True,  # don't want convergence warnings
                                 stepwise=True)  # set to stepwise
    
    stepwise_fit.summary()
    
    forecast_values = stepwise_fit.predict(n_periods=100)
    
    forecast_values_df = pd.DataFrame(forecast_values)
    forecast_values_df.columns  = [name]
    
    ds_test = ds_test.reset_index(drop=True)

    splits = name.split("_")
    o = splits[0]
    d = splits[1]
    sb.set_style('darkgrid')
    forecast_values_df.plot(color = '#F4511E', legend = True, label = col + " (Forecast)", title = "Flights count between " + o + " and " + d )
    ds_test.plot(color = '#3949AB', legend = True, label = col + " (Actual)")    
    path = r'C:/Users/Chethan/Desktop/test/'
    path = path + str(col_number) + "_" + name + ".png"
    plt.savefig(path,bbox_inches='tight')
#    plt.show()
    plt.clf()
    
    # MSE
    from sklearn.metrics import mean_squared_error
    mse = mean_squared_error(ds_test, forecast_values)
    
    print("\nMean squared error: ", mse)

col_number = 1
for col in ds:
    name = str(col)
    iterate(name, ds[col], col_number)
    col_number = col_number + 1
    
