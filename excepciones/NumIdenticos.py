# creacion clase de excepcion personalizada
class NumIdenticos(Exception):
    def __init__(self, mensaje):
        self._mensaje = mensaje
