from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contador_teclados = 0
    
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    @property
    def id_teclado(self):
        return self._id_teclado

    @id_teclado.setter
    def id_teclado(self, id_teclado):
        self._id_teclado = id_teclado

    def __str__(self):
        return f'Teclado id: {self._id_teclado}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'

''' 
teclado1 = Teclado('HP','USB')
print (teclado1)

teclado2 = Teclado('ACER','WIFI')
print (teclado2)

 '''