from sqlite3 import Cursor
import psycopg2 as bd

conexion = bd.connect(user = 'postgres', password = '030481', host = 'localhost', port = '5432', database = 'db_prueba')
try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s, %s, %s)'
            valores = ('jose', 'ponce', 'jponce@gmail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('juan', 'pineda', 'jpineda@gmail.com', 1)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrió un error, se hizo roolback : {e}')
finally:
    conexion.close()
    print ('transaccion terminada')


