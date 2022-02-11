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
print(next(num1pares))
print(next(num1pares))
print(next(num1pares))
print(next(num1pares))
