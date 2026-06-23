import time
import numpy as np


def main():
    inicio = time.perf_counter()

    np.random.seed(42)

    tamanho = 600

    matriz_a = np.random.rand(tamanho, tamanho)
    matriz_b = np.random.rand(tamanho, tamanho)

    produto = np.dot(matriz_a, matriz_b)

    media = np.mean(produto)
    desvio = np.std(produto)
    soma = np.sum(produto)

    fim = time.perf_counter()

    print("Script: numerico.py")
    print(f"Tamanho da matriz: {tamanho}x{tamanho}")
    print(f"Média: {media:.6f}")
    print(f"Desvio padrão: {desvio:.6f}")
    print(f"Soma: {soma:.6f}")
    print(f"Tempo interno: {fim - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
