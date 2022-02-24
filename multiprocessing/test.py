from multiprocessing import Process
from time import sleep
import time
import numpy as np

def TimeLimiter(func,timeout, *args):
    p = Process(target=func, args=args)
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        print("Ha finalizado por timeout")
        return False
    print("Se ha ejecutado correctamente")
    return True

lista_de_listas=[ [1  ,-4],[12 , 3],[7.2, 5]]

def test(lista_de_listas):
    print("uno:")
    matriz = np.array(lista_de_listas)
    print(matriz)

def test2(lista_de_listas):
    print("dos:")
    time.sleep(3.0)
    matriz = np.array(lista_de_listas)
    print(matriz)

if __name__ == '__main__':
    TimeLimiter(test, 2.5,lista_de_listas) 
    TimeLimiter(test2, 2.9,lista_de_listas) 
    


