
import numpy as np


try:
    np.zeros((2, 3))      # matriz 2x3 só com zeros
    np.ones((3, 3))       # matriz 3x3 só com uns
    np.eye(3)             # matriz identidade 3x3
    np.full((2, 2), 7)    # matriz 2x2 preenchida com 7
    np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
    np.linspace(0, 1, 5)  # 5 valores igualmente espaçados entre 0 e 1
    a  = np.array([[144, 64, 4], [10, 11, 13]])
    c  = a[a > 1]
    a = np.full((10, 10), 0)

    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])  

    a + b     # [11, 22, 33]
    a * b     # [10, 40, 90]
    a ** 2    # [1, 4, 9]
    np.sqrt(b)  # raiz quadrada
    np.mean(b)  # média
    #b = np.sqrt(a[0])
    print(a)
except:
    print( "ERRO: ")
