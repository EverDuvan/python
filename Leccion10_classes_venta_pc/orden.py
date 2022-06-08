from computador import Computador


class Orden:
    contador_ordenes = 0

    def __init__(self, computadores):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadores = computadores

    @property
    def id_orden(self):
        return self._id_orden

    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden

    @property
    def computadores(self):
        return self._computadores

    @computadores.setter
    def computadores(self, computadores):
        self._computadores = computadores

    def agregar_computador (self, computador):
        self._computadores.append(computador)

    def __str__(self):
        computadores_str = ''
        for computador in self._computadores:
            computadores_str += computador.__str__()
        return f'''
            Orden: {self._id_orden}
            Computadores: {computadores_str}
        '''

    



