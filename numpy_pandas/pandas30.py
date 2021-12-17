import pandas as pd 

#genera dataframe a partir del documento csv
df = pd.read_csv("EnterpriseSurvey.csv")
#muestra el df
print (df)

#muestra los  primeros datos del df o la cantidad que se ponga entre los parentecis 
df.head()

#muestra los ultimos datos del df o la cantidad que se ponga entre los parentecis 
df.tail(4)

#muestra informacion estadistica del df, como la media el minimo y el maximo 
df.describe()

#muestra la informacion de la columna definida entre llaves 
df["Variable_category"]

#muestra la informacion de las columnas definidas entre dos llaves separados por coma (lista de encabezados) 
df[["Variable_category","Industry_code_ANZSIC06"]]

#muestra la fila definida por el indice entre llaves 
df.iloc[4]

#muestra el rango de filas (desde-hasta) definido entre llaves separado por dos puntos, con el indice como dato
df.iloc[2:6]

#cambia el indice generado automaticamente por el de una columna  (en este caso Variable_code)
df = pd.read_csv("EnterpriseSurvey.csv", index_col="Variable_code")
#muestra el df
df

#genera un nuevo df con los valores de columna y filas que se decean (columnas: H05 y H38. filas: Industry_code_NZSIOC y Value en este caso)
df.loc[["H05","H38"],["Industry_code_NZSIOC","Value"]]

#filtrado por caracteristicas se selecciona la columna (Industry_aggregation_NZSIOC) para este caso y que 
#caracteristica debe cumplir (Level 1) en este caso
df[df["Industry_aggregation_NZSIOC"]=="Level 1"]

# varias condiciones
df[(df["Industry_aggregation_NZSIOC"]=="Level 1")&(df["Units"]=="Dollars (millions)")]

#busca una cadena de texto especifica dentro de una columna (classes) para este caso 
df[df["Industry_code_ANZSIC06"].str.contains("classes")]

df = pd.read_csv("EnterpriseSurvey.csv")
def fecha_nivel(Year):
    fechan=Year/2
    return fechan
df["fechan"] = df["Year"].apply(fecha_nivel)

