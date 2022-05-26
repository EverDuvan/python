import pandas as pd 

print ('genera dataframe a partir del documento csv')
df = pd.read_csv("EnterpriseSurvey.csv")
#muestra el df
print (df)

print ('muestra los  primeros datos del df o la cantidad que se ponga entre los parentecis ')
print (df.head())

print ('muestra los ultimos datos del df o la cantidad que se ponga entre los parentecis ')
print(df.tail(4))

print ('muestra informacion estadistica del df, como la media el minimo y el maximo ')
print(df.describe())

print ('muestra la informacion de la columna definida entre llaves ')
print(df["Variable_category"])

print ('muestra la informacion de las columnas definidas entre dos llaves separados por coma (lista de encabezados) ')
print (df[["Variable_category","Industry_code_ANZSIC06"]])

print ('muestra la fila definida por el indice entre llaves ')
print (df.iloc[4])

print ('muestra el rango de filas (desde-hasta) definido entre llaves separado por dos puntos, con el indice como dato')
print (df.iloc[2:6])

print ('cambia el indice generado automaticamente por el de una columna  (en este caso Variable_code)')
df = pd.read_csv("EnterpriseSurvey.csv", index_col="Variable_code")
#muestra el df
print (df)

print ('genera un nuevo df con los valores de columna y filas que se decean (columnas: H05 y H38. filas: Industry_code_NZSIOC y Value en este caso)')
print (df.loc[["H05","H38"],["Industry_code_NZSIOC","Value"]])

print ('filtrado por caracteristicas se selecciona la columna (Industry_aggregation_NZSIOC) para este caso y que ')
print ('caracteristica debe cumplir (Level 1) en este caso')
print (df[df["Industry_aggregation_NZSIOC"]=="Level 1"])

print ('varias condiciones')
print (df[(df["Industry_aggregation_NZSIOC"]=="Level 1")&(df["Units"]=="Dollars (millions)")])

print ('busca una cadena de texto especifica (classes) dentro de una columna (Industry_code_ANZSIC06) para este caso ')
print (df[df["Industry_code_ANZSIC06"].str.contains("classes")])

df = pd.read_csv("EnterpriseSurvey.csv")
def fecha_nivel(Year):
    fechan=Year/2
    return fechan
df["fechan"] = df["Year"].apply(fecha_nivel)

