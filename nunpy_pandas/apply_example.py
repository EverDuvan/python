import pandas as pd

datos = {"nombre": ["Juan", "María", "Pedro", "Ana"],
         "edad": [10, 20, 30, 40],
         "nota": [30, 60, 80, 90]}
df = pd.DataFrame(datos)
print (df)

def calcular_calificacion_final(fila):
    calificacion_final = (fila["nota"] + 2) + (fila["edad"] * 3)
    return calificacion_final

# Aplicar la función a cada fila del DataFrame usando apply()
df["calificacion_final"] = df.apply(calcular_calificacion_final, axis=1)
df["nota"] = df["nota"].apply(lambda x: x + 5)
print(df)
