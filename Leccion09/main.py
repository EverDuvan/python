from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print (objeto)
    print (f'tipo de objeto: {type(objeto)}')

empleado = Empleado('juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'sistemas')
imprimir_detalles(gerente)
