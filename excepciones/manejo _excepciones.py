from NumIdenticos import NumIdenticos

print ('ejemplo 01')
try:
    10/0
except Exception as e:
    print (f'error: {e}')

######################################
print ('ejemplo 02')
resultado = None
a = 10
b = 0
try:
    resultado = a/b
except Exception as e:
    print (f'Error: {e}')
print (resultado)
print ('continuamos')

######################################
print ('ejemplo 03')
resultado = None
a = '10'
b = 0
try:
    resultado = a/b
except Exception as e:
    print (f'Error: {e}')
print (resultado)
print ('continuamos')

######################################
print ('ejemplo 04')
resultado = None
a = '10'
b = 0
try:
    resultado = a/b
except ZeroDivisionError as e:
    print (f'Error ZeroDivisionError: {e}, {type(e)}')
except TypeError as e:
    print (f'error TypeError: {e}, {type(e)}')
except Exception as e:
    print (f'Error classe padre: {e}, {type(e)}')
print (resultado)
print ('continuamos')

######################################
print ('ejemplo 05')
resultado = None
try:
    #a = int(input('primer numero: '))
    #b = int(input('segundo numero: '))
    resultado = a/b
except ZeroDivisionError as e:
    print (f'Error ZeroDivisionError: {e}, {type(e)}')
except TypeError as e:
    print (f'error TypeError: {e}, {type(e)}')
except Exception as e:
    print (f'Error classe padre: {e}, {type(e)}')
print (resultado)
print ('continuamos')

######################################
print ('ejemplo 06')
resultado = None
try:
    #a = int(input('primer numero: '))
    #b = int(input('segundo numero: '))
    resultado = a/b
except ZeroDivisionError as e:
    print (f'Error ZeroDivisionError: {e}, {type(e)}')
except TypeError as e:
    print (f'error TypeError: {e}, {type(e)}')
except Exception as e:
    print (f'Error classe padre: {e}, {type(e)}')
    # bloque 'else' y 'finally' son opcionales:
else:
    print ('No hubo ninguna excepcion')
finally:
    print ('finally siempre se ejecuta (esto es un ejemplo)')
print (resultado)
print ('continuamos')

######################################
print ('ejemplo 07 Class Numidenticos')
resultado = None 
try:
    a = int(input('primer numero: '))
    b = int(input('segundo numero: '))
    if a == b:
        raise NumIdenticos('numeros identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print (f'Error ZeroDivisionError: {e}, {type(e)}')
except TypeError as e:
    print (f'error TypeError: {e}, {type(e)}')
except Exception as e:
    print (f'Error classe padre: {e}, {type(e)}')
    # bloque 'else' y 'finally0' son opcionales:
else:
    print ('No hubo ninguna excepcion')
finally:
    print ('finally siempre se ejecuta (esto es un ejemplo)')
print (resultado)
print ('continuamos')


