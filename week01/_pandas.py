import pandas as pd
#Pandas é uma Biblioteca python que facilita a manipulação, análise e limpeza dos dados
#Trabalhando com tabelas(como planilhas do excel ou tabelas SQL)

try :
    data = {
    'nome': ['Ana', 'Bruno', 'Carlos'],
    'idade': [23, 35, 45],
    'cidade': ['Luanda', 'Lobito', 'Lubango']
    }

    df = pd.DataFrame(data)
    print(df)

    print("\n------------\n")

    # Pegar os dados de um arquivo
    df = pd.read_json("files/folha.json")
    # df = pd.read_json("files/folha.json")
    # df = pd.read_excel("files/folha.xlsx")
    # df = pd.read_csv("files/folha.csv")

    # add coluna
    df['salario'] = [2000, 3000, 4000]
    df[df["salario"] > 10] # filtrar dados

    df.drop('object', axis=1, inplace=True) # eliminar um coluna
    df.drop(0, axis=0, inplace=True) # eliminar um linha
    
    # substituir os valores nulos de uma coluna
    df["cidade"] = df["cidade"].fillna("Sem")
    df["idade"] = df["idade"].fillna(0)

    # exportar para um arquivo
    df.to_csv("./files/saida.csv", index=False) # exportar para um arquivo csv
    print(df.sort_values("name", ascending=False))
except Exception as e:
     print(f"Ocorreu um erro: {e}")