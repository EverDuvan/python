import pandas as pd


datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Luisa'],
         'Edad': [25, 30, 35, 28],
         'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}

df = pd.DataFrame(datos)

data = df.loc[df['Edad'] >= 30]
#print(data)

data2 = df.iloc[0].tolist()
print(data2)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3].split('-')
print(parts)
n = parts[1]
print(n)