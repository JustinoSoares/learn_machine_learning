import pandas as pd

try:
    #Ler o arquivo
    df = pd.read_csv("files/filmes.csv")
    # Pegar os 10 primeiros filmes com maior notas
    df = df.sort_values("nota", ascending=False).head(10)
    # pegar filmes depois de 2015 
    df = df[df['ano'] > 2015]
    #agrupar por genero e trazer a media das notas
    df = df.groupby(['genero', 'titulo', 'ano', 'duracao'])['nota'].mean()
    print("\n-------Agrupamento por genero e mostrando a nota---------\n")
    # exportar o conteudo para um outro arquivo csv
    df.to_csv("saida.csv")
    print(df) 
except Exception as e:
    print(f"Erro : {e}")