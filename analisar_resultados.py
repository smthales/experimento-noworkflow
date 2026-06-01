import csv
from collections import defaultdict


ARQUIVO_ENTRADA = "results/resultados_preliminares.csv"
ARQUIVO_SAIDA = "results/resumo_preliminar.csv"


def converter_cpu(valor):
    return float(valor.replace("%", ""))


def main():
    dados = defaultdict(list)

    with open(ARQUIVO_ENTRADA, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            chave = (linha["script"], linha["categoria"], linha["modo"])

            dados[chave].append(
                {
                    "tempo": float(linha["tempo_real_seg"]),
                    "memoria": int(linha["memoria_kb"]),
                    "cpu": converter_cpu(linha["cpu_percentual"]),
                }
            )

    medias = {}

    for chave, execucoes in dados.items():
        media_tempo = sum(e["tempo"] for e in execucoes) / len(execucoes)
        media_memoria = sum(e["memoria"] for e in execucoes) / len(execucoes)
        media_cpu = sum(e["cpu"] for e in execucoes) / len(execucoes)

        medias[chave] = {
            "tempo": media_tempo,
            "memoria": media_memoria,
            "cpu": media_cpu,
        }

    linhas_saida = []

    scripts = sorted(set(chave[0] for chave in medias))

    for script in scripts:
        categoria = None

        tradicional = None
        noworkflow = None

        for chave, valores in medias.items():
            nome_script, nome_categoria, modo = chave

            if nome_script == script:
                categoria = nome_categoria

                if modo == "tradicional":
                    tradicional = valores
                elif modo == "noworkflow":
                    noworkflow = valores

        if tradicional and noworkflow:
            overhead_tempo = (
                (noworkflow["tempo"] - tradicional["tempo"])
                / tradicional["tempo"]
            ) * 100

            overhead_memoria = (
                (noworkflow["memoria"] - tradicional["memoria"])
                / tradicional["memoria"]
            ) * 100

            linhas_saida.append(
                {
                    "script": script,
                    "categoria": categoria,
                    "tempo_medio_tradicional": round(tradicional["tempo"], 4),
                    "tempo_medio_noworkflow": round(noworkflow["tempo"], 4),
                    "overhead_tempo_percentual": round(overhead_tempo, 2),
                    "memoria_media_tradicional_kb": round(tradicional["memoria"], 2),
                    "memoria_media_noworkflow_kb": round(noworkflow["memoria"], 2),
                    "overhead_memoria_percentual": round(overhead_memoria, 2),
                    "cpu_medio_tradicional_percentual": round(tradicional["cpu"], 2),
                    "cpu_medio_noworkflow_percentual": round(noworkflow["cpu"], 2),
                }
            )

    with open(ARQUIVO_SAIDA, mode="w", newline="", encoding="utf-8") as arquivo:
        campos = linhas_saida[0].keys()
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(linhas_saida)

    print(f"Resumo salvo em {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()
