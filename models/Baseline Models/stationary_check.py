# Importing libraries
import numpy as np, pandas as pd
# import matplotlib.pyplot as plt

range1 = [i for i in range(0,100)]
ds =  pd.read_csv(r"C:/Users/Chethan/Downloads/preprocessed_dataset_final.csv", usecols = range1)

df_all_data = ds.copy()

# Drop time column
df = ds.drop(['day'], axis = 1)


# Removing columns with same origin and destination
for col in df:
    od = str(col)
    od_list = od.split("_")
    o = od_list[0]
    d = od_list[1]
    
    if o == d:
        del df[col]
        
# Removing constant columns      
df_no_constants = df.loc[:, (df != df.iloc[0]).any()]
 
ds = df_no_constants

# Splitting the dataset into train & test subsets
n_obs = 120
ds_train, ds_test = ds[:-n_obs], ds[-n_obs:]

from statsmodels.tsa.stattools import adfuller

stat = 0
non_stat = 0

def adf_test(ds):
    dftest = adfuller(ds, autolag='AIC')
    adf = pd.Series(dftest[0:4], index = ['Test Statistic','p-value','# Lags','# Observations'])

    for key, value in dftest[4].items():
       adf['Critical Value (%s)'%key] = value
#     print (adf)

    p = adf['p-value']
    if p <= 0.05:
#         print("\nSeries is Stationary")
        global stat
        stat = stat + 1
    else:
        global non_stat
        non_stat = non_stat + 1
        print(ds.head())
#         print("\nSeries is Non-Stationary")

for i in ds_train.columns:
#     print("Column: ",i)
#     print('--------------------------------------')
    adf_test(ds_train[i])
#     print('\n')
print("Stationarity first time with no differencing")    
print("Stat ", stat)
print("Non stat", non_stat)
print("\n")

stat = 0
non_stat = 0

# Differencing all variables to get rid of Stationarity
ds_differenced = ds_train.diff().dropna()

# Removing constant columns      
ds_differenced = ds_differenced.loc[:, (ds_differenced != ds_differenced.iloc[0]).any()]

# Running the ADF test once again to test for Stationarity
for i in ds_differenced.columns:
#     print("Column: ",i)
#     print('--------------------------------------')
    adf_test(ds_differenced[i])
#     print('\n')

print("Stationarity after first differencing")    
print("Stat ", stat)
print("Non stat", non_stat)
print("\n")

#print(ds_differenced['KLDJ_LFPG'])

















stat = 0
non_stat = 0

ds_differenced = ds_differenced.diff().dropna()


# Running the ADF test for the 3rd time to test for Stationarity
for i in ds_differenced.columns:
#     print("Column: ",i)
#     print('--------------------------------------')
    adf_test(ds_differenced[i])
#     print('\n')

print("Stationarity after second differencing")    
print("Stat ", stat)
print("Non stat", non_stat)
print("\n")

# stat = 0
# non_stat = 0

# ds_differenced = ds_differenced.diff().dropna()


# # Running the ADF test for the 4th time to test for Stationarity
# for i in ds_differenced.columns:
# #     print("Column: ",i)
# #     print('--------------------------------------')
#     adf_test(ds_differenced[i])
# #     print('\n')

# print("Stationarity after third differencing")    
# print("Stat ", stat)
# print("Non stat", non_stat)
# print("\n")


# import numpy as np, pandas as pd
# import matplotlib.pyplot as plt, seaborn as sb
# import pmdarima as pm

# # Importing Dataset
# range1 = [i for i in range(1,1001)]
# ds =  pd.read_csv(r'/home/chve882b/preprocessed_dataset_final.csv', usecols = range1)

# # Splitting the dataset into train & test subsets
# n_obs = 120  # 20% test data
# ds_train, ds_test = ds[:-n_obs], ds[-n_obs:]


# max_diff = 0
# for col in ds:
#     diff = pm.arima.ndiffs(x= ds_train[col], test = 'adf', max_d = 3)
#     print(diff)
#     if diff > max_diff:
#         max_diff = diff
        
# print("maximum: ",max_diff)