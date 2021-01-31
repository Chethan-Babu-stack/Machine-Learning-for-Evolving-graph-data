import pandas as pd

# Importing Dataset
range1 = [i for i in range(1,1048)]
df =  pd.read_csv(r"C:/Users/Chethan/Downloads/preprocessed_dataset_final.csv" , usecols = range1)


for col in df:
    od = str(col)
    od_list = od.split("_")
    o = od_list[0]
    d = od_list[1]
    
    if o == d:
        del df[col]
        
df_no_constants = df.loc[:, (df != df.iloc[0]).any()]
        

print(df.iloc[:,0])





#path = r'/home/chve882b/raw_data/' # use your path
#all_files = glob.glob(path + "*.csv")
#
#print("All files read")
#
#li = [] 
#for filename in all_files:
#    df = pd.read_csv(filename, index_col=None, header=0, low_memory=False, usecols = [5,6,9])
#    li.append(df)
#
#data = pd.concat(li, axis=0, ignore_index=True)
#data = data.dropna()
#
#print("Entire data loaded")
#
#def countOD(df, o_d):
#    for i in range(len(df)):
#        temp_o_d = str(data.iloc[i]['origin']) + "_" + str(data.iloc[i]['destination'])
#        o_d[temp_o_d] += 1
#    
#    d = pd.DataFrame([o_d])
#    return d
#
#""" Column names are edges: If A is origin and B is the destination, 
#then A_B will be the column saying the count of edges starting from A to B
#
#Rows are indexed by date
#"""
## List of dates which would be used as row indices
#dates = list(dict.fromkeys(data["day"]))
#
#print(len(dates))
#
## List of ORIGIN_DESTINATION for column names
#o_d = dict()
#for i in range(len(data)):
#    temp_o_d = str(data.iloc[i]['origin']) + "_" + str(data.iloc[i]['destination'])
#    
#    if temp_o_d not in o_d.keys():
#        o_d[temp_o_d] = 0
#
## Create an empty dataframe with column names        
#out_data = pd.DataFrame(columns = list(o_d.keys()),dtype='uint8')
#
#print("Column names are formed")
#
## Loop through all the dates and count the flights between Origin and destination    
#for d in range(len(dates)):
#    df = data[data["day"] == dates[d]]
#    o_d = dict.fromkeys( o_d, 0 )  # set all dictionary values to zero
#    temp_data = countOD(df, o_d)
#    out_data = out_data.append(temp_data)
#    
## Add dates column to dataframe
#out_data['day'] = dates 
#
## Convert day into Datetime
#out_data['day']=pd.to_datetime(out_data['day'],format='%Y-%m-%d')
#
#print("OD counts computed for all columns")
#
## Set day as index to dataframe
#out_data.set_index('day',inplace=True)
#
#print("Date indices are set")
#
#out_data.to_csv('preprocessed_dataset_final.csv', sep=',')
#
#print("Data saved")
