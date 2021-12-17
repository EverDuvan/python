import numpy as np

M = [[3, 8, 1, 0], [-1, 4, 7, 5], [3, 2, 0, 5], [9, 12, 65, 10]]

print("================================")

for i in range(len(M)):
  for j in range(len(M)):
    if i==0 or i== 2:
      print("",M[i][j], end="  ") 
    elif i==3:
      print("",M[i][j], end=" ")
    else:
      print(M[i][j], end="   ") 

  print("")

print("================================")

for i in range(0,4):
  for j in range(0,4):
    if M[i][j]<10 and M[i][j] >= 0:
      print("",M[i][j], end="  ") 
    if M[i][j] >= 10:
      print(M[i][j], end="  ")
    if M[i][j]<0:
      print (M[i][j], end="  ")

  print("")
print("================================")