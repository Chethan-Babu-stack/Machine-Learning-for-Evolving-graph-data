import numpy as np
import pandas as pd
import pickle as pkl

def load_flights_data(dataset):
    flt_adj = pd.read_csv(r'C:\Users\Chethan\Desktop\TUD\TUD Sem 3\T-GCN-master\T-GCN-master\data\od_adj_latest.csv',header=None)
    adj = np.mat(flt_adj)
    range1 = [i for i in range(1,1001)]
    flt_tf = pd.read_csv(r'C:\Users\Chethan\Desktop\TUD\TUD Sem 3\T-GCN-master\T-GCN-master\data\o_d_timeseries.csv', usecols = range1)
    return flt_tf, adj


def preprocess_data(data, time_len, rate, seq_len, pre_len):
    train_size = int(time_len * rate)
    train_data = data[0:train_size]
    test_data = data[train_size:time_len]
    
    trainX, trainY, testX, testY = [], [], [], []
    for i in range(len(train_data) - seq_len - pre_len):
        a = train_data[i: i + seq_len + pre_len]
        trainX.append(a[0 : seq_len])
        trainY.append(a[seq_len : seq_len + pre_len])
    for i in range(len(test_data) - seq_len -pre_len):
        b = test_data[i: i + seq_len + pre_len]
        testX.append(b[0 : seq_len])
        testY.append(b[seq_len : seq_len + pre_len])
      
    trainX1 = np.array(trainX)
    trainY1 = np.array(trainY)
    testX1 = np.array(testX)
    testY1 = np.array(testY)
    return trainX1, trainY1, testX1, testY1
    
