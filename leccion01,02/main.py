from Persona import Persona

#import Aritmetica
#import Rectangulo
#import Cubo
# dar formato a la imprecion .center para centrar la cadena,
# (50,'*') 50 cantidad de caracteres a repetir a lado y lado,
# en este caso asteriscos <

print (' creacion de objetos '.center(50,'*'))
persona1 = Persona('karla','Gomez', 30 )
print (persona1.mostrar_Detalle())

#como eliminar un objeto, no es comun su uso (se debe agregar su constructor
# en la clase Persona 'en este caso')
#print (' eliminacion de objetos '.center(50,'-') )
#del persona1

# para imprimir el lugar desde el que se esta ejecutando el codigo print
# (__name__)
#print (__name__)