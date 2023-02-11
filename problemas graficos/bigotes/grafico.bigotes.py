import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas graficos\\bigotes\\bigotes.csv")

# crear la grafica con el nombre de las cordenadas y pasarle sus valores / data
sns.boxplot(x="categoria", y="valor", data=df)

# mostrar el grafico
plt.show()
