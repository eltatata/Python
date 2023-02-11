import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas graficos\\ingresos\\ingresos.csv")

total_ingresos = df["ingresos"].sum()

print(f"Total de ingresos: {total_ingresos}")

# crear la grafica con el nombre de las cordenadas y pasarle sus valores / data
sns.barplot(x="fuente", y="ingresos", data=df)

# mostrar el grafico
plt.show()
