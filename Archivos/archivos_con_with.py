import encodings
from ManejoArchivos import ManejoArchivos

# with open('prueba.txt','r', encoding='utf8') as archivo:
with ManejoArchivos('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())
