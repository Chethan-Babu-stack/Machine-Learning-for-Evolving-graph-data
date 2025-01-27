# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:02:47 2020

@author: Chethan
"""

# Simple Multivariate Time-Series Forecasting

# Importing libraries
import numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sb

# Importing Dataset
df =  pd.read_csv(r"C:/Users/Chethan/Downloads/preprocessed_dataset_final.csv" , usecols = [5,6])
#, usecols = [0,1,2,3,4,5,6]
ds = df.drop(['day'], axis = 1)

# Visualize the trends in data
sb.set_style('darkgrid')
ds.plot(kind = 'line', legend = 'reverse', title = 'Visualizing OD connectivity over time')
plt.legend(loc = 'upper right', shadow = True, bbox_to_anchor = (1.35, 0.8))
plt.show()

## Dropping Temperature & Relative Humidity as they do not change with Time
#ds.drop(['Temperature','Rel_Humidity'], axis = 1, inplace = True)

# Again Visualizing the time-series data
#sb.set_style('darkgrid')
#ds.plot(kind = 'line', legend = 'reverse', title = 'Visualizing Sensor Array Time-Series')
#plt.legend(loc = 'upper right', shadow = True, bbox_to_anchor = (1.35, 0.8))
#plt.show()


#ds = df.drop(['day'], axis = 1)
# Splitting the dataset into train & test subsets
n_obs = 120
ds_train, ds_test = ds[:-n_obs], ds[-n_obs:]

# Augmented Dickey-Fuller Test (ADF Test) to check for stationarity
from statsmodels.tsa.stattools import adfuller

stat = 0
non_stat = 0
def adf_test(ds):
    dftest = adfuller(ds, autolag='AIC')
    adf = pd.Series(dftest[0:4], index = ['Test Statistic','p-value','# Lags','# Observations'])

    for key, value in dftest[4].items():
       adf['Critical Value (%s)'%key] = value
    print (adf)

    p = adf['p-value']
    if p <= 0.05:
        print("\nSeries is Stationary")
        global stat
        stat = stat + 1
    else:
        global non_stat
        non_stat = non_stat + 1
        print("\nSeries is Non-Stationary")


for i in ds_train.columns:
    print("Column: ",i)
    print('--------------------------------------')
    adf_test(ds_train[i])
    print('\n')
    
print("Stat ", stat)
print("Non stat", non_stat)

stat = 0
non_stat = 0

# Differencing all variables to get rid of Stationarity
ds_differenced = ds_train.diff().dropna()

# Running the ADF test once again to test for Stationarity
for i in ds_differenced.columns:
    print("Column: ",i)
    print('--------------------------------------')
    adf_test(ds_differenced[i])
    print('\n')

# Now cols: 3, 5, 6, 8 are non-stationary
ds_differenced = ds_differenced.diff().dropna()


# Running the ADF test for the 3rd time to test for Stationarity
for i in ds_differenced.columns:
    print("Column: ",i)
    print('--------------------------------------')
    adf_test(ds_differenced[i])
    print('\n')
    
    
    
    
    
# Fitting the VAR model to the 2nd Differenced Data
from statsmodels.tsa.api import VAR

model = VAR(ds_differenced)
results = model.fit()
#results.summary()

# Forecasting for 100 steps ahead
lag_order = results.k_ar
predicted = results.forecast(ds_differenced.values[-lag_order:], n_obs)
forecast = pd.DataFrame(predicted, index = ds.index[-n_obs:], columns = ds.columns)


# Plotting the Forecasted values
#p1 = results.plot_forecast(1)
#p1.tight_layout()

# Inverting the Differencing Transformation
def invert_transformation(ds, df_forecast, second_diff=False):
    for col in ds.columns:
        # Undo the 2nd Differencing
        if second_diff:
            df_forecast[str(col)] = (ds[col].iloc[-1] - ds[col].iloc[-2]) + df_forecast[str(col)].cumsum()

        # Undo the 1st Differencing
        df_forecast[str(col)] = ds[col].iloc[-1] + df_forecast[str(col)].cumsum()

    return df_forecast

forecast_values = invert_transformation(ds_train, forecast, second_diff=False)

# ======================================   Visualization  ==========================================
# Actual vs Forecasted Plots
#fig, axes = plt.subplots(nrows = int(len(ds.columns)/2), ncols = 2, dpi = 100, figsize = (10,10))
#
#for i, (col,ax) in enumerate(zip(ds.columns, axes.flatten())):
#    forecast_values[col].plot(color = '#F4511E', legend = True, ax = ax).autoscale(axis =' x',tight = True)
#    ds_test[col].plot(color = '#3949AB', legend = True, ax = ax)
#
#    ax.set_title('Column: ' + col + ' - Actual(Blue) vs Forecast(Red)')
#    ax.xaxis.set_ticks_position('none')
#    ax.yaxis.set_ticks_position('none')
#
#    ax.spines["top"].set_alpha(0)
#    ax.tick_params(labelsize = 6)
#
#plt.tight_layout()
#plt.savefig('actual_forecast.png')
#plt.show()

col_number = 77
for col in ds_test:
    splits = str(col).split("_")
    o = splits[0]
    d = splits[1]
    sb.set_style('darkgrid')
    forecast_values[col].plot(color = '#F4511E', legend = True, label = col + " (Forecast)", title = "Flights count between " + o + " and " + d )
    ds_test[col].plot(color = '#3949AB', legend = True, label = col + " (Actual)")
#    plt.show()
    path = r'C:/Users/Chethan/Desktop/test/'
    path = path + str(col_number) + "_" + str(col) + ".png"
    plt.savefig(path,bbox_inches='tight')
    col_number = 1 + col_number
    plt.clf()

# MSE
from sklearn.metrics import mean_squared_error
from numpy import asarray as arr
mse = mean_squared_error(ds_test, forecast_values)

print("\nMean squared error: ", mse)




k=0
for i in range(0,200):
    range1 = [i for i in range(k,5+k)]
    print(range1)
    k = k + 5 