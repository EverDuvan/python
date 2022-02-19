n = 10
impares = [n for n in range (n+1) if n%2 !=0]
print(*impares, sep=", ")

print ('generadores')

def pares (maximo):
    num=0
    lista_pares=[]
    while num<maximo:
        lista_pares.append(num*2)
        num+=1
    return lista_pares

num_pares=pares(10)
print (num_pares)

print ('*************************************')

def paresgen(max):
    num1=0
    while num1<max:
        yield num1*2
        num1+=1


num1pares=paresgen(10)
print (paresgen) # imprime el objeto generador 

print(next(num1pares)) # primera iteracion del generador
print(next(num1pares)) # segunda iteracion del generador
print(next(num1pares)) # asi sucecivamente hasta 
print(next(num1pares))

g=paresgen(10)
# imprime una lista de las iteraciones de el generador 
lista=list(g)
# imprime una tupla de las iteraciones de el generador
tupla=tuple(g)
print (lista)
print (tupla)


