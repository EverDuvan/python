from orden import Orden
from computador import Computador
from monitor import Monitor
from raton import Raton
from teclado import Teclado


teclado1 = Teclado('HP','BLUETOOTH')
raton1 = Raton('ACER','USB')
monitor1 = Monitor('LG',20)
computador1 = Computador('office',monitor1,teclado1,raton1)

teclado2 = Teclado('HP','BLUETOOTH')
raton2 = Raton('ACER','USB')
monitor2 = Monitor('SHARP',22)
computador2 = Computador('gaming',monitor2,teclado2,raton2)

teclado3 = Teclado('GENIUS','BLUETOOTH')
raton3 = Raton('BND','USB')
monitor3 = Monitor('SONY',22)
computador3 = Computador('gamer',monitor3,teclado3,raton3)

Computadores1 = [computador1,computador2]
orden1 = Orden(Computadores1)
#print (orden1)

orden1.agregar_computador(computador3)
print (orden1)

computadores2 = [computador3,computador1]
orden2 = Orden(computadores2)
print (orden2)

