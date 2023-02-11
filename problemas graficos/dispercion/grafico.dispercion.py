import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas graficos\\dispercion\\dispercion.csv")

# crear la grafica con el nombre de las cordenadas y pasarle sus valores / data
sns.scatterplot(x="tiempo", y="dinero", data=df)

# mostrar el grafico
plt.show()
