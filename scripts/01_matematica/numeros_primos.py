import time

inicio = time.time()

primos = []

for n in range(2, 10000):
    primo = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            primo = False
            break

    if primo:
        primos.append(n)

fim = time.time()

#print(len(primos))
#print("Tempo:", fim - inicio)