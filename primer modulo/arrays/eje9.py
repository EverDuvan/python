import numpy as np

Matrix = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

NuevaMatrix=np.split(Matrix,3)


NuevaMatrix = np.array_split(Matrix, 3)
print(NuevaMatrix)



