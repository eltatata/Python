# ----------------------------------------------------------------------------------------------------
# OBTENER LA INFORMACION CON PANDAS

import pandas as pd

df = pd.read_csv("archivos\\CSV\\data.csv")
# ----------------------------------------------------------------------------------------------------
# VISUALIZAR DATA FRAME

print(df, "\n")
# ----------------------------------------------------------------------------------------------------
# OBTENER LOS VALORES DE LA COLUMNA NOMBRES

print(df['name'], "\n")
# ----------------------------------------------------------------------------------------------------
# ORDENAR DATA FRAME POR EDADES

# asecendente
df_sort = df.sort_values("age")

# descendente
df_sort = df.sort_values("age", ascending=False)

print(df_sort, "\n")
# ----------------------------------------------------------------------------------------------------
# CONCATENAR con "concat"

data = {'name': ['Pedro', 'Pablo'],
        'age': [5, 60],
        'nacionality': ['Colombia', 'Iran']}

df2 = pd.DataFrame(data)

df_concat = pd.concat([df, df2])

print(df_concat, "\n")
# ----------------------------------------------------------------------------------------------------
# HEAD() TAIL()

# accerder desde la primera fila
print(df.head(1), "\n")

# accerder desde la ultima fila
print(df.tail(1), "\n")
# ----------------------------------------------------------------------------------------------------
# SABER CANTIDAD DE FILAS Y COLUMNAS

row, col = df.shape

print(f"Cantidad filas: {row}, Cantidad columnas: {col}\n")
# ----------------------------------------------------------------------------------------------------
# OBTENER NUMEROS ESTADISTICOS

df_info = df.describe()

print(df_info, "\n")
# ----------------------------------------------------------------------------------------------------
# LOC, ILOC

# acceder a una elemento especifico de el df con "loc"
elemento = df.loc[0]
# propiedades de el elemento
name, age, nacionality = elemento

print(elemento)
print(name, age, nacionality, "\n")

# acceder a la edad de la fila 2 con "iloc"
print(df.iloc[2, 1], "\n")

# acceder a todas las filas de una columna "age"
print(df.iloc[:,1], "\n")

# acceder a filas donde la edad es mayor que 30
print(df.loc[df["age"]>40,:], "\n")

# acceder a filas donde la edad es menor que 50
print(df.loc[df["age"]<50,:])