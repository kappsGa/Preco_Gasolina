# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv("gasolina.csv")
sns.lineplot(data=gasolina_df, x="dia", y="venda", color="#FF5733")
plt.title("Preço da Gasolina")

plt.savefig("gasolina.png")