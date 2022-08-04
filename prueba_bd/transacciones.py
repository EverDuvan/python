from sqlite3 import Cursor
import psycopg2 as bd

conexion = bd.connect(user = 'postgres', password = '030481', host = 'localhost', port = '5432', database = 'db_prueba')
try:
    # autocommit por defecto es igual a False por lo que no se pone si este es el caso 
    # conexion.autocommit = False
    

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s, %s, %s)'
    valores = ('jose', 'ponce', 'jponce@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('juan', 'pineda', 'jpineda@gmail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print ('transaccion terminada')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo roolback : {e}')
finally:
    conexion.close()


