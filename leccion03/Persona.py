class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
# metodo string para devolver una cadena en este caso con
# los valores de las variables, todo esto con solo dar print y el objeto
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}'

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
        self._nombre = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


# creacion calse hija Empleado
class Empleado(Persona):
# se agreaga el constructor para declarar como hijo de la
# calse persona
    def __init__(self, nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self._sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}, sueldo: {self.sueldo}'

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo


#se crea un objeto empleado 'hijo' de la clase persona
#empleado1 = Empleado('carlos', 30, 2000)
#print(f'{empleado1.nombre} {empleado1.edad} {empleado1.sueldo}')
