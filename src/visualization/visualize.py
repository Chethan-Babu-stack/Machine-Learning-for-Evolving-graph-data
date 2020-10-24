
### VISUALIZE.PY

import networkx as nx
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


# function to create graph object from dataframe using NetworkX
def create_graph_object(df, directionality):
    graph = nx.from_pandas_edgelist(df, source = 'origin', \
                                 target = 'destination', create_using = directionality)
    print(graph)
    return graph   


# function to create variable pos, that contains the position of each node
def create_pos_variable(df, m):
    
    # Assign the longitude to mx and the latitude to my
    # Because you assign it to the m, which is the basemap, the coordinates are 
    # recalculated to the size of m
    mx, my = m(df['longitude_1'].values, df['latitude_1'].values)
#    print(mx)
    pos = {}
    for count, elem in enumerate (df['origin']):
         pos[elem] = (mx[count], my[count])

    mx, my = m(df['longitude_2'].values, df['latitude_2'].values)
#    print(mx)
#    pos = {}
    for count, elem in enumerate (df['destination']):
         pos[elem] = (mx[count], my[count])
         
    return pos

# function to create a node size list dependent on degree 
def node_size_degree(graph):
    
    # calculate degree of each node and save as dictionary
    degree = dict(graph.degree())

    # create a list with node sizes by multiplying the node degree with 1.5 for each node
    node_size_list = []
    for h in degree.values():
        node_size_list = node_size_list + [h * 1.5]
    
    return node_size_list

# function to draw the nodes and edges with specific parameters
def draw_nodes_and_edges(graph, pos, node_size, node_visibility, edge_visibility, ncolor='#FF6585', ecolor='#4B8BBE', ewidth = 2):
    
    # draw the nodes of graph on the map and set other parameters for layout     
#    try:
    nx.draw_networkx_nodes(graph, pos, node_size = node_size, node_color = ncolor, alpha = node_visibility)
#    except Exception as err: 
#        pass                 
    # draw the edges of graph on the map and set other parameters for layout
#    try:
    nx.draw_networkx_edges(graph, pos, edge_color = ecolor, width = ewidth, alpha = edge_visibility)
#    except Exception as err: 
#        pass
    

#%% Function to draw network on the world map

def visualize_on_worldmap(dataframe, directionality=nx.Graph(), node_size=20, hub_nr=0, node_visibility=0.8, edge_visibility=0.1):
     
    # create graph object from dataframe
    graph = create_graph_object(dataframe, directionality)
    
    # print graph info
    graph_info = nx.info(graph)
    print(graph_info)

    # draw mercator projection as background and set size
    plt.figure(figsize = (15,20))
    m = Basemap(projection='merc',
                llcrnrlon=-180,
                llcrnrlat=-80,
                urcrnrlon=180,
                urcrnrlat=80)

    # include coastlines, countries and boundaries
    m.drawcoastlines()
    m.drawmapboundary()
    m.drawcountries()

    # include longitude and latitude lines if you want
    m.drawparallels(np.arange(-90,90,30))
    m.drawmeridians(np.arange(-180,180,60))

    # create variable pos, that contains the position of each node
    pos = create_pos_variable(dataframe, m)   
    
    # draw the nodes and edges on the map and set other parameters for layout
    draw_nodes_and_edges(graph, pos, node_size, node_visibility, edge_visibility)
    
    # show plot
    plt.show()

# edges: dataframe(origin, destination, count)
# vertices: dict(airports:count)
# positions: list(list(airport, latitude, longitude))
#    show(temp, edges, positions)
def show(temp):
    graph = create_graph_object(temp, nx.Graph())
    node_size = node_size_degree(graph)
    visualize_on_worldmap(temp, node_size = node_size)
