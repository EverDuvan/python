import pandas as pd

lista = [1, 2, 3, 4, 5]
factor = 2

# Usar función lambda con map()
resultado = list(map(lambda x: x * factor, lista))
print(f'resultado 01: {resultado} \n')


lista = [1, 2, 3, 4, 5]

# Usar función lambda con filter()
resultado = list(filter(lambda x: x % 2 == 0, lista))
print(f'resultado 02: {resultado} \n')

#######################################


serie = pd.Series([1, 2, 3, 4, 5])

# Usar función lambda con apply()
resultado = serie.apply(lambda x: x ** 2)
print(f'resultado 03: \n{resultado}')

#######################################

