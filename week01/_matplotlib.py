import matplotlib.pyplot as plt
import numpy as np

try : 
    #x = [0, 1, 2, 3, 4]
    #categorias = ["A", "B", "C", "D", "E"]
    
    x = [1, 2, 3, 4, 5]
    y1 = [i**2 for i in x]
    y2 = [i*2 for i in x]

    plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, posição 1
    plt.plot(x, y1)
    plt.title("Quadrado")

    plt.subplot(1, 2, 2)  # posição 2
    plt.bar(x, y2)
    plt.title("Multiplicado por 2")

    plt.tight_layout()  # evita sobreposição
    plt.show()
except Exception as e:
    print(e)
    
