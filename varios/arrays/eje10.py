
import numpy as np

matrix= np.array([9,11,8,22,7,33,6,44,5,55,4,66,3,77,2,88,1,99])  

x = np.where(matrix%2 == 0)
print(matrix)
print("indices:",x)

valores=np.array(matrix[x])
print("valores:",valores)