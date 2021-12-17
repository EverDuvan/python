class persona:
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'persona: {self._nombre} {self._apellido} {self._edad}')

#como eliminar un objeto para liberar memoria
    def __del__(self):
        print(f'persona: {self._nombre} {self._apellido}')



if __name__ == '__main__':
    persona1= persona('juan','perez',28)
    persona1.nombre = 'juan carlos'
    persona1.apellido = 'lara'
    persona1.edad = 30
    persona1.mostrar_detalle()

    #propiedad para determinar cual el el modulo que se está ejecutando
    print(__name__)
