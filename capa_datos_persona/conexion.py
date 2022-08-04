from multiprocessing import pool
from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'db_prueba'
    _USERNAME = 'postgres'
    _PASSWORD = '030481'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_COM = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool (cls._MIN_CON, cls._MAX_COM,
                                                      host=cls._HOST, 
                                                      user=cls._USERNAME, 
                                                      password=cls._PASSWORD, 
                                                      port=cls._DB_PORT, 
                                                      database=cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool {e}')
        else:
            return cls._pool    
    
    @classmethod
    def obtenerConexion(cls):
        pass

        '''         
        if cls._conexion is None:
            try:
                cls._conexion  = bd.connect(host=cls._HOST, 
                                            user=cls._USERNAME, 
                                            password=cls._PASSWORD, 
                                            port=cls._DB_PORT, 
                                            database=cls._DATABASE)
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.ERROR(f'Ocurrió un error al obtener la conexion {e}')
                sys.exit()
        else:
            return cls._conexion
        '''
    '''   
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.ERROR(f'Ociurrió una excepcion al obtener un cursor {e}')
                sys.exit()
        else:
            return cls._cursor
    '''

if __name__ == '__main__':
    pass


