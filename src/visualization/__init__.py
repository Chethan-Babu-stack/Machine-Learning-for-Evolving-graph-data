import os
os.environ["PROJ_LIB"] = 'C:\\Users\\Chethan\\Anaconda3\\Library\\share'

import pandas as pd
import visualize as v

#change the path to one specific file
path = r'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/Research Project/Machine-Learning-for-Evolving-graph-data/data/raw/flightlist_20200401_20200430.csv'

df = pd.read_csv(path, index_col=None, header=0)

#df.dtypes

df = df.reindex(columns=["callsign","origin","destination","day","latitude_1","longitude_1","latitude_2","longitude_2"])

#df = df[(df["origin"]!="\\N") & (df["destination"]!="\\N")]

df = df.dropna()

# Origin Airports list
#origin_airports = list(dict.fromkeys(df["origin"]))

#df = df["callsign","origin","destination","latitude_1","longitude_1","latitude_2","longitude_2"].groupby(["day","origin"]).size().reset_index(name='counts')

# Destination airports
#destination_airports = list(dict.fromkeys(df["destination"]))

dates = list(dict.fromkeys(df["day"]))

#for d in range(len(dates)):
temp = df[df["day"] == dates[0]]
day = dates[0]
del temp["day"]

# Flights between origin and destination
edges = temp.groupby(["origin","destination"]).size().reset_index(name='counts')

# Flights count in each airport
#vertices = list(dict.fromkeys(temp["destination"]))
#vertices.append(list(dict.fromkeys(temp["origin"])))

vertices = dict()
positions = []
for index, r in temp.iterrows():
    if r["origin"] in vertices.keys():
        vertices[r["origin"]] += 1
    else:
        vertices[r["origin"]] = 1
        positions.append([r["origin"],r["latitude_1"],r["longitude_1"]])
        
    if r["destination"] in vertices.keys():
        vertices[r["destination"]] += 1
    else:
        vertices[r["destination"]] = 1
        positions.append([r["destination"],r["latitude_2"],r["longitude_2"]])

# edges: dataframe(origin, destination, count)
# vertices: dict(airports:count)
# positions: list(list(airport, latitude, longitude))
        
#del temp['latitude_2']
#del temp['longitude_2']
#
#temp = temp.rename(columns={'latitude_1':'latitude', 'longitude_1':'longitude'})
#temp = temp[:2]
v.show(temp, edges, positions)

