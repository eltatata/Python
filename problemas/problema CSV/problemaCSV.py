# ----------------------------------------------------------------------------------------------------
# CAMBIAR EL TIPO DE DATO DE UNA COLUMNA

import pandas as pd

df = pd.read_csv("problemas\\problema CSV\\data.csv")

print(df, "\n")

print(type(df['age'][0]))

# cambiando del tipo de dato a cadena de texto
df['age'] = df['age'].astype(str)

print(type(df['age'][0]))

# cambiar el valor de algun dato
df['name'].replace("Isco", "Carvajal", inplace=True)

print("\n", df)

# eliminar filas con datos faltantes
df = df.dropna()

print("\n", df)

# eliminar filas repetidas
df = df.drop_duplicates()

print("\n", df)

# crar un nuevo csv con el "df" resultante
df.to_csv("problemas\\problema CSV\\problema_csv.csv")