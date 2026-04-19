import pandas as pd

# Ler, transformar e salvar
df = pd.read_csv("vendas.csv")
df["total"] = df["qtd"] * df["preco"]
df_mensal = df.groupby("mes")["total"].sum().reset_index()
df_mensal.to_excel("relatorio_mensal.xlsx", index=False)
