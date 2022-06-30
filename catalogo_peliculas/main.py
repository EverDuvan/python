from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
    try:
        print ('opciones: ')
        print ('1. Agragar pelicula')
        print ('2. Listar peliculas')
        print ('3. Eliminar catalogo peliculas')
        print ('4. Salir')
        opcion = int(input('Escribe tu opcion (1-4):'))
        print (' ')

        if opcion == 1:
            nombre_pelicula =input('Ingrese el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        
        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar_peliculas()            

    except Exception as e:
        print (f'Ocurrió un error: {e}')
        print ('Vuelva a digitar una oopcion')
        option = None
else:
        print ('Salir del programa')

