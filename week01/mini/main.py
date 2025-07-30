import pandas as pd

try:
    df = pd.read_csv("files/filmes.csv")
    #df = df.sort_values("nota", ascending=False).head(10)
    print(df) 
    print("\n------\n")
    df.groupby("genero")["nota"].min()
    #df = df[df["ano"] > 2015]
    df.to_csv("saida.csv")
    print(df) 
except Exception as e:
    print(f"Erro : {e}")