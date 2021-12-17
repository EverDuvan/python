""" Modulo para la definición de funciones
    para crear y graficar grafos
  Ever Duvan Hernandez 
    Junio 2-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
import networkx as nx
import matplotlib.pyplot as plt
import csv

with open("letras.csv") as uni:
  csv_leer = csv.reader(uni)
  Gn = nx.Graph(csv_leer)

print(Gn.nodes())

nx.draw(Gn, with_labels = True)

print("=================ARISTAS===============")
print(Gn.edges())

plt.show()




  