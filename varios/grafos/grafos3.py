import networkx as nx
import matplotlib.pyplot as plt
import csv

with open("Ejercicio3.csv") as uni:
  csv_leer = csv.reader(uni)
  Gn = nx.Graph(csv_leer)

print(Gn.nodes())

nx.draw_circular(Gn,with_labels=True)

print("================================")
print(Gn.edges())

plt.show()