import networkx as nx
import matplotlib.pyplot as plt

Gn = nx.Graph()

Gn.add_edge('Tom_Hanks','Gari_Sinlse', weight = 3, label = "4", color = "blue")
Gn.add_edge('Ed_Harris','Gari_Sinlse', weigth = 1, label = "1")
Gn.add_edge('Tom_Hanks','Bill_Paxton', weigth = 1, label = "1")
Gn.add_edge('Tom_Hanks','Kevin_Bacon', weigth = 1, label = "1")
Gn.add_edge('Bill_Paxton','Gari_Sinlse', weigth = 1, label = "1")
Gn.add_edge('Kevin_Bacon','Gari_Sinlse', weigth = 1, label = "1")

weigths=[Gn[x][y]["weigth"] for x,y in Gn.edges()]
etiqueta=[Gn[x][y]["label"]for x,y in Gn.edges()]
pos=nx.spring_layout(Gn)
nx.draw_networkx_nodes(Gn,pos, node_size=500, node_color="orange")
nx.draw_networkx_edges(Gn,pos,width=weigths,alpha=0.5,edge_color="black")
nx.draw_networkx_edge_labels(Gn,pos,edge_labels={(x,y):Gn[x][y]["label"]for x,y in Gn.edges()})
nx.draw_networkx_labels(Gn,pos)
plt.show()