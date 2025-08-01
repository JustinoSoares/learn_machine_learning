import numpy as np 
import pandas as pd

try :

    np.random.seed(42)
    size = 20

    #criando dados ficticios
    produtos = ["camisa", "calça", "chapéu", "vestido", "sapato"]
    clientes = ["João", "Carlos", "Julia", "Carla", "Santos"]

    # criar um data frame com 20 vendas

    df = pd.DataFrame({
        'clientes' : np.random.choice(clientes, size=size),
        'produtos' : np.random.choice(produtos, size=size),
        'quantidade' : np.random.randint(1, 5, size=size),
        'preco' : np.random.uniform(50, 300, size=size).round(1)
    })
    #df = df.sort_values("cliente")


    df["total_vendas"] = np.round(df["quantidade"] * df["preco"], 2)
    
    venda_por_client = df.groupby('clientes')["total_vendas"].sum()

    media = df["total_vendas"].mean()
    desvio = df["total_vendas"].std()
    
    print(f"Media: {media.round(2)}")
    print(f"Desvio: {desvio.round(2)}")
    print("\nfiltrar a cima da media\n")
    cima_da_media = df[df["total_vendas"] > media]
    print(cima_da_media)
except Exception as e :
    print(e)