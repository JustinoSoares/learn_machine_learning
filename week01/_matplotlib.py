import matplotlib.pyplot as mtl

try : 
    x = [10, 11, 13]
    y = [16, 14, 20]
    mtl.plot(x, y)
    mtl.title("Exemplo")
    mtl.xlabel("eixo x")
    mtl.ylabel("eixo y")
    mtl.show()
except Exception as e:
    print(e)