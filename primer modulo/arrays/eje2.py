import numpy as np

lista0=[42]
Tupla0=(56)
Tupla1=(1,2,3,4,5,6)
Tupla2=([[1,2,3],[3,4,5]])
Tupla3=([[[1,2,3],[4,3,6]],[[1,9,5],[7,5,8]]])

print(lista0)
print(Tupla0)
print(Tupla1)
print(Tupla2)
print(Tupla3)
print("========================")
Matriz0a=np.array([42])
Matriz0=np.array(56)
Matriz1=np.array([1,2,3,4,5,6])
Matriz2=np.array([[1,2,3],[3,4,5]])
Matriz3=np.array([[[1,2,3],[4,3,6]],[[1,9,5],[7,5,8]]])

print("1",Matriz0a)
print("Dimension",Matriz0a.ndim) 
print("2",Matriz0)
print("Dimension",Matriz0.ndim) 
print("3",Matriz1)
print("Dimension",Matriz1.ndim) 
print("========================")
print("4",Matriz2)
print("Dimension",Matriz2.ndim) 
print("========================")
print("5",Matriz3)
print("Dimension",Matriz3.ndim) 




"""
matriz = [[1, 2], [3, 4], [5, 6]]
print(matriz)

#for i in range(0,len(matriz)):
#  num=matriz[i]
#  print(num)
#print("")

matriz=[[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]],[[13,14],[15,16],[17,18]]]

print(matriz[2][0][0])
print(matriz[2][0][0])

"""