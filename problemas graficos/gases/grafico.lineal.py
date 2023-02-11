import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas graficos\\gases\\gases.csv")

# obtener el index del valor mas alto de gases
max_index = df['gases'].idxmax()

# acceder a una elemento especifico de el df con "loc" y si indice
fecha, gases = df.loc[max_index]

# crear la grafica con el nombre de las cordenadas y pasarle sus valores / data
sns.lineplot(x="fecha", y="gases", data=df)

# marcar el punto mas alto en la grafica
plt.plot(fecha, gases, "o")

# mostrar el grafico
plt.show()
