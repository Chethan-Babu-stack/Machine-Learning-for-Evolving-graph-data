# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:31:07 2021

@author: Chethan
"""
# Importing libraries
import numpy as np, pandas as pd
# import matplotlib.pyplot as plt

range1 = [i for i in range(1,1001)]
ds =  pd.read_csv(r"C:/Users/Chethan/Downloads/preprocessed_dataset_no_commonOD_no_constants_all_stationary.csv", usecols = range1)


o_d_list = list(ds)


rows = cols = len(o_d_list)

od_adj = np.zeros(shape=(rows, cols), dtype=np.uint8)


for i in range(0, rows):
    o_d_row = str(o_d_list[i])
    for j in range(0, cols):
        o_d_col = str(o_d_list[j])
        
        if o_d_row[5:] == o_d_col[0:4]:
            od_adj[i,j] = 1
        
res_df = pd.DataFrame(data = od_adj)

res_df.to_csv(r"C:\Users\Chethan\Desktop\TUD\TUD Sem 3\Research Project\DataSet\Preprocessed\od_adj.csv", sep=",",header=False, index = False)
