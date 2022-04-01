from re import M


class MiClase:
    variable_clase='variable clase'
    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print (MiClase.variable_clase)

MiClase.metodo_estatico()



''' 
print (MiClase.variable_clase)
MiClase=MiClase('valor objeto')
print(MiClase.variable_instancia)
print(MiClase.variable_clase)

MiClase.variable_clase2= ('otro valor de variable de clase')
print (MiClase.variable_clase2)

 '''