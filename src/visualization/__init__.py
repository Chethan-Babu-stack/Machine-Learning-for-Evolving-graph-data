import os
os.environ["PROJ_LIB"] = 'C:\\Users\\Chethan\\Anaconda3\\Library\\share'

import pandas as pd
import visualize as v
import glob

#change the path to one specific file
#path = r'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/Research Project/Machine-Learning-for-Evolving-graph-data/data/raw/flightlist_20200401_20200430.csv'
#
#df = pd.read_csv(path, index_col=None, header=0)
#
#df = df.reindex(columns=["callsign","origin","destination","day","latitude_1","longitude_1","latitude_2","longitude_2"])
#
#df = df.dropna()
#
#dates = list(dict.fromkeys(df["day"]))
#
##for d in range(len(dates)):
#temp = df[df["day"] == dates[0]]
#day = dates[0]
#del temp["day"]
#
## Flights between origin and destination
#edges = temp.groupby(["origin","destination"]).size().reset_index(name='counts')
#
#vertices = dict()
#positions = []
#for index, r in temp.iterrows():
#    if r["origin"] in vertices.keys():
#        vertices[r["origin"]] += 1
#    else:
#        vertices[r["origin"]] = 1
#        positions.append([r["origin"],r["latitude_1"],r["longitude_1"]])
#        
#    if r["destination"] in vertices.keys():
#        vertices[r["destination"]] += 1
#    else:
#        vertices[r["destination"]] = 1
#        positions.append([r["destination"],r["latitude_2"],r["longitude_2"]])
#
#v.show(temp, edges, positions)

def graph_with_date():
    d = input("""Enter the date for visualization in YYYYMMDD format. 
              Example: 20201501 (for January 15th 2020)
              Range: January 1st 2019 till August 31st 2020: """)
    input_date = d
    
    d = d[:-2]

    path = r'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/Research Project/DataSet/' # use your path
    all_files = glob.glob(path + "*" + d + "*.csv")

    print(all_files)
    
    # Will be use later
    li = [] 
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
        
    df = df.dropna()
#    dates = list(dict.fromkeys(df["day"]))
#    vis_date = "2020-04-01 00:00:00+00:00"
    input_date = input_date[0:4] + "-" + input_date[4:6] + "-" + input_date[6:] + " 00:00:00+00:00"
    print(input_date)
    temp = df[df["day"] == input_date]
    v.show(temp)

while True:   
# print options to user:
    choice = input("""What do you want to do?0
    0\tSee the visualization of a particular date.
    1\tExit program.
    enter answer (0/1): """)
    
    # evaluate user choice and proceed accordingly
    if choice == "0": 
        graph_with_date()
    elif choice == "1": # Exit program 
        print("Thank you for using this program.")
        break 
    else:
        print("Please enter correct input.")
