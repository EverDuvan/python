from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computador:
    contador_computadores = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computador.contador_computadores += 1
        self._id_computador = Computador.contador_computadores
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton 
    
    @property
    def id_computador(self):
        return self._id_computador

    @id_computador.setter
    def id_computador(self, id_computador):
        self._id_computador = id_computador

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''
        computador {self._nombre} id: {self._id_computador}
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''

teclado1 = Teclado('HP','BLUETOOTH')
raton1 = Raton('ACER','USB')
monitor1 = Monitor('Hp',15)

computador1 = Computador('HP',monitor1,teclado1,raton1)
print (computador1)

