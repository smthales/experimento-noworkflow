import time

inicio = time.time()

with open("dados.txt", "w") as f:
    for i in range(100000):
        f.write(f"{i}\n")

fim = time.time()

#print("Tempo:", fim - inicio)