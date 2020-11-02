
# VISUALIZE.PY

import networkx as nx
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

import nx_altair as nxa

# Function to create graph object from dataframe using NetworkX
def create_graph_object(df, directionality):
    graph = nx.from_pandas_edgelist(df, source = 'origin', \
                                 target = 'destination', create_using = directionality)
#    print(graph)
    return graph   


# Function to create variable pos, that contains the position of each node
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

    for count, elem in enumerate (df['destination']):
         pos[elem] = (mx[count], my[count])
         
    return pos

# Function to create a node size list dependent on degree 
def node_size_degree(graph):
    
    # Calculate degree of each node and save as dictionary
    degree = dict(graph.degree())

    # Create a list with node sizes by multiplying the node degree with 1.5 for each node
    node_size_list = []
    for h in degree.values():
        node_size_list = node_size_list + [h * 1.5]
    
    return node_size_list

# Function to draw the nodes and edges with specific parameters
def draw_nodes_and_edges(graph, pos, node_size, node_visibility, edge_visibility, ncolor='#FF6585', ecolor='#4B8BBE', ewidth = 2):
    
    # draw the nodes of graph on the map and set other parameters for layout     
    nx.draw_networkx_nodes(graph, pos, node_size = node_size, node_color = ncolor, alpha = node_visibility)               
    # draw the edges of graph on the map and set other parameters for layout
    nx.draw_networkx_edges(graph, pos, edge_color = ecolor, width = ewidth, alpha = edge_visibility)

# Function to draw network on the world map

def visualize_on_worldmap(dataframe, directionality=nx.MultiGraph(), node_size=20, hub_nr=0, node_visibility=0.8, edge_visibility=0.1,date="",video=0):
     

    # create graph object from dataframe
    graph = create_graph_object(dataframe, directionality) 
    # print graph info
    graph_info = nx.info(graph)
#    print(graph_info)

    # draw mercator projection as background and set size
    plt.figure(figsize = (15,20))
    plt.text(0.1,0.1,date,size=15,color="purple")
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
    
    # Save images for video
    if video == 1:
        path = r'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/screenshots/'
        path = path + date + ".png"
        plt.savefig(path,bbox_inches='tight')
    else:
        plt.show()
    
    plt.close()

def show(temp,date,video):
    graph = create_graph_object(temp, nx.MultiGraph())
    node_size = node_size_degree(graph)
    visualize_on_worldmap(temp, node_size = node_size,date=date,video=video)
