import numpy as np
import pandas as pd
import datetime

#lista_de_listas=[[1,-4],[12,3],[7.2,5]]

print("Matriz creada con una lista de listas:")
lista_de_listas=[[1  ,-4],[12 , 3],[7.2, 5]]

matriz = np.array(lista_de_listas)
print(matriz)

## df con la fecha y hora actual

now = datetime.datetime.now()
data = {'fecha': [now.strftime('%Y-%m-%d')],
        'hora': [now.strftime('%H:%M:%S')]}
df = pd.DataFrame(data)
print(df)
df = df.reindex(columns=['hora', 'fecha'])
print (df)