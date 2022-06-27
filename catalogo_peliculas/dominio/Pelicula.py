from mailbox import NoSuchMailboxError


class Pelicula:
    contador_peliculas = 0

    def __init__(self, nombre):
        Pelicula.contador_peliculas += 1
        self._id_pelicula = Pelicula.contador_peliculas
        self._nombre = nombre

    @property
    def id_pelicula(self):
        return self._id_pelicula

    @id_pelicula.setter
    def id_pelicula(self, id_pelicula):
        self._id_pelicula = id_pelicula 

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre 

    def __str__(self):
        return f'Pelicula id: {self._id_pelicula}, Nombre: {self._nombre}'


