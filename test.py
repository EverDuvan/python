import pandas as pd


datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Luisa'],
         'Edad': [25, 30, 35, 28],
         'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}

df = pd.DataFrame(datos)

data = df.loc[df['Edad'] >= 30]
#print(data)

data2 = df.iloc[0].tolist()
print(data2)
