n = 10
impares = [n for n in range (n+1) if n%2 !=0]
print(*impares, sep=", ")
