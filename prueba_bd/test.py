import psycopg2

conexion = psycopg2.connect(user = 'postgres', password = '030481', host = 'localhost', port = '5432', database = 'db_prueba')

try:
    with conexion:
        with conexion.cursor() as cursor:
            # SELECT * FROM _ en la sentencia se escribe la tabla que se trae homologados en este caso
            # WHERE = URL %s _ para escribir la fila especifica a traer, URL en este caso
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            category_id = input ('escriba el numero de id : ')
            cursor.execute(sentencia, (category_id,))
            # fetchall = regresa todos los registros 
            # fetchone = regresa un solo registro 
            registros = cursor.fetchall() 
            for registro in registros:
                print(registros)
except Exception as e:
    print(f'Ocurrió el siguiente error: {e}')
finally:
    conexion.close()


