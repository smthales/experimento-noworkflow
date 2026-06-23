import time

inicio = time.time()

with open("dados.txt") as f:
    linhas = f.readlines()

fim = time.time()

#print(len(linhas))
#print("Tempo:", fim - inicio)