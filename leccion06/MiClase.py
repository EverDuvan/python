from re import M


class MiClase:
    variable_clase='variable clase'
    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia

print (MiClase.variable_clase)
MiClase=MiClase('valor objeto')
print(MiClase.variable_instancia)
print(MiClase.variable_clase)