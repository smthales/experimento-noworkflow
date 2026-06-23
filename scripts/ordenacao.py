import bisect
import random
import time


def busca_binaria(lista_ordenada, alvo):
    indice = bisect.bisect_left(lista_ordenada, alvo)

    if indice < len(lista_ordenada) and lista_ordenada[indice] == alvo:
        return indice

    return -1


def main():
    inicio = time.perf_counter()

    random.seed(42)

    tamanho_lista = 5_000
    quantidade_buscas = 200

    numeros = [random.randint(1, 1_000_000) for _ in range(tamanho_lista)]
    lista_ordenada = sorted(numeros)

    alvos = [random.randint(1, 1_000_000) for _ in range(quantidade_buscas)]

    encontrados = 0

    for alvo in alvos:
        if busca_binaria(lista_ordenada, alvo) != -1:
            encontrados += 1

    fim = time.perf_counter()

    print("Script: ordenacao.py")
    print(f"Quantidade de números: {tamanho_lista}")
    print(f"Quantidade de buscas: {quantidade_buscas}")
    print(f"Valores encontrados: {encontrados}")
    print(f"Menor valor: {lista_ordenada[0]}")
    print(f"Maior valor: {lista_ordenada[-1]}")
    print(f"Tempo interno: {fim - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
