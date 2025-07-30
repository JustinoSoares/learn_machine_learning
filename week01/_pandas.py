import pandas as pd

try :
    df = pd.read_json("files/folha.json")

    # add coluna
    df['salario'] = [2000, 3000, 4000]
    #df = pd.DataFrame(data)
    #df.drop('cidade', axis=1, inplace=True) # eliminar um coluna
    df.drop(0, axis=0, inplace=True) # eliminar um linha
    df.to_csv("./files/saida.csv", index=False)
    df["cidade"] = df["cidade"].fillna("Sem")
    df["idade"] = df["idade"].fillna(0)
    print(df.sort_values("name"))
except Exception as e:
     print(f"Ocorreu um erro: {e}")