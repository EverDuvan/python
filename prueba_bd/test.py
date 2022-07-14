import psycopg2

conexion = psycopg2.connect(user = 'xxxx', password = 'xxxx', host = 'localhost', port = '5432', database = 'data_procesing2')

try:
    with conexion:
        with conexion.cursor() as cursor:
            # SELECT * FROM _ en la sentencia se escribe la tabla que se trae homologados en este caso
            # WHERE = URL %s _ para escribir la fila especifica a traer, URL en este caso
            sentencia = 'SELECT * FROM homologados WHERE category_id = %s'
            category_id = input ('escriba el numero de category_id: ')
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


