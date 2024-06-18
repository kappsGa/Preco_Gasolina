import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv("gasolina.csv")
sns.lineplot(data=gasolina_df, x="dia", y="venda")

plt.savefig("gasolina.png")