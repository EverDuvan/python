import numpy as np

Matriz1D = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

Matriz2D = Matriz1D.reshape(6,3)

Matriz3D = Matriz2D.reshape(3,3,2)
print("==========1============")
print(Matriz1D)
print("===========2============")
print(Matriz2D)
print("============3===========")
print(Matriz3D)