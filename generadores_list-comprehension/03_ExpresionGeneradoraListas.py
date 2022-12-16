# Expresión generadora (es un generador anónimo)
multiplicacion = (valor*valor for valor in range(4))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
# print(next(multiplicacion))

# También se puede pasar una expresión generadora a una función (sin paréntesis)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')

print ('*********************************************')

# También podemos usar una lista o cualquier otro iterador
lista = ['Juan','Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

print ('*********************************************')

# Crear un string a partir de un generador creado a partir de una lista
lista = ['Karla','Gomez', 22]
# Definimos una función para incrementar el contador
contador = 0
def incremetar():
    global contador
    contador += 1
    return contador
# La primera para es el yield, la segunda es el for, entre paréntesis
generador = (f'{incremetar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')


