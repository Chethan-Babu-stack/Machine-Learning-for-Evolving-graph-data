# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:28:19 2020

@author: Chethan
"""

# Importing libraries
import numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sb

# Importing Dataset
range1 = [i for i in range(0,2)]
df =  pd.read_csv(r"C:/Users/Chethan/Downloads/preprocessed_dataset_final.csv", usecols = range1)
#ds = df.drop(['day'], axis = 1)


col_number = 1
for col in df:
    if col != 'day':
        splits = str(col).split("_")
        o = splits[0]
        d = splits[1]
        # Visualize the trends in data
        sb.set_style('darkgrid')
    #    ds[col].plot(kind = 'line', legend = 'reverse', title = 'Flights count between airports ' + o + " and " + d + " over time" )
    #    plt.legend(loc = 'upper right', shadow = True, bbox_to_anchor = (1.35, 0.8))
    #    plt.show()
        df.plot.line(x='day', y= col)
        plt.show()
#        path = r'C:/Users/Chethan/Desktop/test/'
#        path = path + str(col_number) + "_" + str(col) + ".png"
#        plt.savefig(path,bbox_inches='tight')
        col_number = 1 + col_number
        plt.clf()