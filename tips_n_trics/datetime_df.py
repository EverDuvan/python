import pandas as pd
import datetime

datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Luisa'],
         'Edad': [25, 30, 35, 28],
         'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}

df = pd.DataFrame(datos)
print (df)
print ('\n' + ' df.loc '.center(50, '*') + '\n')
data = df.loc[df['Edad'] >= 30]
print(data)
print ('\n' + ' df.iloc '.center(50, '*') + '\n')
data2 = df.iloc[0].tolist()
print(data2)

print ('\n' +' words '.center(50, '*') + '\n')
words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(f'pieces: {pieces}')
parts = pieces[3].split('-')
print(f'parts: {parts}')
n = parts[1]
print(n)

print ('\n' + ' datetime '.center(50, '*') + '\n')
now = datetime.datetime.now()
data = {'fecha': [now.strftime('%Y-%m-%d')],
        'hora': [now.strftime('%H:%M:%S')]}
df = pd.DataFrame(data)
print(f'{df}' + '\n')
