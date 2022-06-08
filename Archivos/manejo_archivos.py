# crear y escribir en archivo

# 'r' = (read) abre un archivo para solo lectura
# 'a' = (Append) abre un archivo para agregar contenido o lo crea si no existe 
# 'w' = (Write) abre un archivo para escribir en el o lo crea si no existe
# 'x' = (Create) cra un archivo, devuelve un error si ya existe 

####################################
from encodings import utf_8


print (' Ejemplo 1 '.center(40,'#'))

try:
    archivo = open('prueba.txt','w', encoding = 'utf_8') # se crea o abre un archivo 
    archivo.write('linea 01- ingresar texto de prueba\nhola ')
    archivo.write('linea 02- texto con tilde = árbol ')
except Exception as e:
    print (f'Error: {e}')
finally :
    archivo.close()
    print ('fin del archivo')

####################################
print (' Ejemplo 2 '.center(40,'#'))

try:
    archivo = open('prueba.txt','r', encoding = 'utf_8')
    print (archivo.read()) # .read() -> se puede poner la cantidad de caracteres a leer
    #print (archivo.readline()) # para leer una sola linea 
    #print (archivo.readline()) # para leer mas lineas se ponen varios prints
except Exception as e:
    print (f'Error: {e}')
finally :
    archivo.close()
    print ('fin del archivo 2')

####################################
print (' Ejemplo 3 '.center(40,'#'))

try:
    archivo = open('prueba.txt','r', encoding = 'utf_8')
    print (archivo.readlines()) # .readlines()[0] devuelve una llista de las
    # lineas se puede pasar un indice de la linea requerida en los corchetes
     
    #for linea in archivo: # for para recorrer todas las lineas de texto 
        #print (linea)
except Exception as e:
    print (f'Error: {e}')
finally :
    archivo.close()
    print ('fin del archivo 2')

####################################
print (' Ejemplo 4 '.center(40,'#'))

try:
    archivo = open('prueba.txt','w', encoding = 'utf_8')
    archivo2 = open('copia.txt', 'a', encoding = 'utf_8')
    archivo2.write(archivo.read())
    
except Exception as e:
    print (f'Error: {e}')
finally :
    archivo2.close()
    archivo.close()
    print ('fin del archivo 4')
