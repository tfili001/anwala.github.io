import matplotlib.pyplot as plt
import networkx as nx
import networkx as centrality
import math
import matplotlib.colors as colors
import matplotlib.cm as cmx

def initialLabel():
    labels = {}
    labels[0]="0"
    labels[1] = r'$John H$'
    labels[33]="Mr. Hi"

    for i in range(2,33):
        labels[i]=str(i)

    return labels


def display(num):
        pos = nx.spring_layout(G)
        labels = initialLabel()
        last=num
        num=nx.number_connected_components(G)
        colormap = ["red","lightgreen","orange","magenta","blue","yellow","purple"]
        if nx.is_connected(G)==False:
             res = []
             for node in G.nodes():
                 res.append(node)
             comp = G.subgraph(res)
             nx.draw_networkx(comp, pos=pos)

             othersub = G.subgraph([0,1,3,4,5,6,7,10,11,12,13,16,17,19,21])
             nx.draw_networkx(othersub,pos,with_labels=True,node_color=colormap[num-1],font_color='black',labels=labels)
               
        else:
            nx.draw_networkx(G,pos,with_labels=True,node_color=colormap[num-1],font_color='black',labels=labels)

        plt.show()

def GirvanNewman(G):
    num=1
    last=ct=0
    while([G.number_of_edges()==0]): 

        allEdgesBetweenness = nx.edge_betweenness_centrality(G)
        b = allEdgesBetweenness.items()
        list = sorted(b,key=lambda x:x[1],reverse=True)
        ct+=1
        print(ct)
        display(num)
        G.remove_edge(*list[0][0])


G = nx.karate_club_graph()
print("Node Degree")
x=0
for v in G:
    print('%s %s' % (v, G.degree(v)))
    x+=G.degree(v)

GirvanNewman(G)


