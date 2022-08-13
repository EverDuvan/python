from sqlite3 import Cursor
from cursor_del_pool import CursorDelPool
from persona import Persona
from conexion import Conexion
from logger_base import log


class PersonaDAO:


    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'persona a insertar: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'persona a actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'persona a eliminada: {persona}')
            return cursor.rowcount


if __name__ == '__main__':
    #    insertar  un registro 
    persona1 = Persona (nombre='raul', apellido='cocio', email='rcocio@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'personas insertadas: {personas_insertadas}')

    # actualizar un registro 
    #persona1 = Persona(nombre='jefry', apellido='cossio', email='jcossio@mail.com', id_persona=1)
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #log.debug(f'personas actualizadas: {personas_actualizadas}')

    # eliminarun registro
    #persona1 = Persona(id_persona=11)
    #personas_eliminadas = PersonaDAO.eliminar(persona1)
    #log.debug(f'personas eliminadas: {personas_eliminadas}')

    # listar registros en BD
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
        



        