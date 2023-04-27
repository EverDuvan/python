import multiprocessing
import math

def sumar_raiz_cuadrada(numeros):
    suma = 0
    for numero in numeros:
        suma += math.sqrt(numero)
    return suma

if __name__ == '__main__':
    # Crear una lista de números
    numeros = list(range(1, 100001))

    # Dividir la lista en cuatro partes iguales
    partes = [numeros[i::4] for i in range(4)]

    # Crear cuatro procesos y asignar una parte de la lista a cada proceso
    procesos = []
    for parte in partes:
        proceso = multiprocessing.Process(target=sumar_raiz_cuadrada, args=(parte,))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos finalicen y obtener el resultado
    suma_total = 0
    for proceso in procesos:
        proceso.join()
        suma_total += proceso.exitcode

    print("La suma de las raíces cuadradas de la lista es: ", suma_total)