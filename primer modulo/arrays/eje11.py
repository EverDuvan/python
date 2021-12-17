#Por medio de una función suma los  valores de 2 matrices
# solo si son el mismo índice, es decir 0 con 0, 1 con 1 y
# así sucesivamente . Investiga que función me ayudaría en numpy a realizar esto

import numpy as np

def mysuma(x,y):
  return x+y

mysuma = np.frompyfunc(mysuma,2,1)

print(mysuma([1, 5, 3, 4], [5, 6, 41, 8]))