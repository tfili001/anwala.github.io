import matplotlib.pyplot as plt
import networkx as nx
import networkx as centrality


def GirvanNewman(G):
    ct=0
    while([G.number_of_edges()==0]): 
        ct+=1        
        print(ct)
        allEdgesBetweenness = nx.edge_betweenness_centrality(G)
        b = allEdgesBetweenness.items()
        list = sorted(b,key=lambda x:x[1],reverse=True)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G,pos)
        #print("All neighbors",nx.clustering(G))
        plt.show()
        G.remove_edge(*list[0][0])

x = 0
G = nx.karate_club_graph()
print("Node Degree")
for v in G:
    print('%s %s' % (v, G.degree(v)))
    x+=G.degree(v)

GirvanNewman(G)
