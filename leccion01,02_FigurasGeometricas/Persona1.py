#crear clase (class)
class Persona:
  #def __init__(self,nombre, apellido,edad, *args, **kwargs): *args para agregar una tupla vacia y **kwargs pra agregar un diccionari
  def __init__(self,nombre, apellido,edad):
    self._nombre = nombre
    self.apellido = apellido
    self.edad = edad

  def mostrar_Detalle(self):
    print (f"metodo persona: {self.nombre} {self.apellido}")


#crear objeto 1
persona1 = Persona('Juan', 'Perez', 38)
print (f"objeto persona1 {persona1.nombre} {persona1.apellido} {persona1.edad}")

#llamar Metodo
persona1.mostrar_Detalle()

"""
como modificar directamente los datos del objeto (indevido) 
persona1.nombre = 'juan carlos'
persona1.apellido = 'juares'
persona1.edad = 25
print (f"objeto persona1 {persona1.nombre} {persona1.apellido} {persona1.edad}")
"""


#crear objeto 2
persona2 = Persona('karla', 'Gomez', 30)
print (f"objeto persona2 {persona2.nombre} {persona2.apellido} {persona2.edad}")