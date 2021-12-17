import numpy as np

matriz3d=np.array([[ [1, 2, 3], [4, 5, 6] ], [ [7, 15, 9], [10, 11, 12] ]])
paresa=[]
imparesa=[]

for idx, x in np.ndenumerate(matriz3d):
  if x%2==0:
    paresa.append(x)
  else:
    imparesa.append(x)
paresa=np.array(paresa)
imparesa=np.array(imparesa)
print(paresa)
print(imparesa)
print("==========================")
pares=[]
impares=[] 
for d1 in matriz3d:
  for d2 in d1:             
    for d3 in d2:
      if d3%2==0:
        pares.append(d3)
      else:
        impares.append(d3)
pares=np.array(pares)
impares=np.array(impares)
print(pares)
print(impares)