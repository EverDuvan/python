from time import time
import numpy as np

def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """
    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret
    
    return wrapper

lista_de_listas=[ [1  ,-4],[12 , 3],[7.2, 5]]

@count_elapsed_time
def test():
    matriz = np.array(lista_de_listas)
    print(matriz)
test()


