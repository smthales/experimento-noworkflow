import time

inicio = time.time()

#resultado = sum(i*i for i in range(5_000_000))
resultado = sum(i*i for i in range(5_000))

fim = time.time()

#print(resultado)
#print("Tempo:", fim - inicio)