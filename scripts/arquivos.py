import csv
import os
import random
import statistics
import time


def gerar_csv(caminho_arquivo, quantidade_linhas):
    random.seed(42)

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "categoria", "valor"])

        for i in range(quantidade_linhas):
            categoria = random.choice(["A", "B", "C"])
            valor = round(random.uniform(10, 1000), 2)
            escritor.writerow([i, categoria, valor])


def processar_csv(caminho_arquivo):
    valores = []
    soma_por_categoria = {"A": 0.0, "B": 0.0, "C": 0.0}
    quantidade_por_categoria = {"A": 0, "B": 0, "C": 0}

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            categoria = linha["categoria"]
            valor = float(linha["valor"])

            valores.append(valor)
            soma_por_categoria[categoria] += valor
            quantidade_por_categoria[categoria] += 1

    media_geral = statistics.mean(valores)
    maior_valor = max(valores)
    menor_valor = min(valores)

    medias_por_categoria = {}

    for categoria in soma_por_categoria:
        medias_por_categoria[categoria] = (
            soma_por_categoria[categoria] / quantidade_por_categoria[categoria]
        )

    return media_geral, maior_valor, menor_valor, medias_por_categoria


def main():
    inicio = time.perf_counter()

    os.makedirs("data", exist_ok=True)

    caminho_arquivo = "data/dados_arquivos.csv"
    quantidade_linhas = 2_000

    gerar_csv(caminho_arquivo, quantidade_linhas)

    media_geral, maior_valor, menor_valor, medias_por_categoria = processar_csv(
        caminho_arquivo
    )

    fim = time.perf_counter()

    print("Script: arquivos.py")
    print(f"Linhas processadas: {quantidade_linhas}")
    print(f"Média geral: {media_geral:.2f}")
    print(f"Maior valor: {maior_valor:.2f}")
    print(f"Menor valor: {menor_valor:.2f}")
    print(f"Médias por categoria: {medias_por_categoria}")
    print(f"Tempo interno: {fim - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
