class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
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

    def mostrar_Detalle(self):
        print(f"metodo: {self._nombre} {self._apellido} {self._edad}")

    def __del__(self):
      print (f'Persona eliminada: {self._nombre} {self._apellido}')

# comprobacion para determinar si se esta ejecutando desde este archivo y
# siendo asi ejecute el codigo acontinuacion
if __name__ == '__main_-':

  persona1 = Persona('juan', 'perez', 28)
  print(persona1.mostrar_Detalle())

  persona1.nombre = 'carlos'
  persona1.apellido = 'velez'
  persona1.edad = 38

  print(persona1.mostrar_Detalle())
  # para imprimir el lugar desde el que se esta ejecutando el codigo print (__name__)
  print (__name__)