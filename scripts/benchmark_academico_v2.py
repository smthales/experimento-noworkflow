# benchmark_academico.py

import subprocess
import time
import psutil
import statistics
import os
import shutil
import pandas as pd

EXECUCOES = 3

SCRIPTS = [
    "01_matematica/soma_de_quadrados.py",
    "01_matematica/numeros_primos.py",
    "02_manipulacao_de_dados_pandas/filtragem.py",
    "02_manipulacao_de_dados_pandas/agrupamento.py",
    "03_machine_learning/regressao_logistica.py",
    "03_machine_learning/random_forest.py",
    "04_arquivos/escrita.py",
    "04_arquivos/leitura.py",
    "05_pipeline_ml/normalizacao_mais_treino.py",
    "05_pipeline_ml/pipeline_completo.py",
    "06_analise_de_dados/analise_exploratoria_dados.py",
    "06_analise_de_dados/limpeza_transformacao_de_dados.py"
]

def tamanho_pasta_noworkflow_global(raiz_busca="."):
    total = 0
    for raiz, dirs, arquivos in os.walk(raiz_busca):
        if ".noworkflow" in raiz:
            for arquivo in arquivos:
                try:
                    total += os.path.getsize(os.path.join(raiz, arquivo))
                except FileNotFoundError:
                    pass
    return total


def executar(script, usar_now=False):

    tempos = []
    memorias = []
    cpus = []
    tamanhos_proveniencia = []

    if usar_now:
        for raiz, dirs, arquivos in os.walk("."):
            if ".noworkflow" in raiz:
                try:
                    shutil.rmtree(raiz)
                except:
                    pass

    for _ in range(EXECUCOES):

        if usar_now:
            comando = ["now", "run", script]
        else:
            comando = ["python3", script]

        inicio = time.perf_counter()
        proc = subprocess.Popen(comando)

        try:
            processo = psutil.Process(proc.pid)
            # Primeira chamada inicializa o contador de CPU do psutil para este processo
            processo.cpu_percent(interval=None)
        except:
            processo = None

        pico_memoria = 0
        pico_cpu = 0

        while proc.poll() is None:
            if processo:
                try:
                    # Captura memória (RSS)
                    memoria = processo.memory_info().rss
                    pico_memoria = max(pico_memoria, memoria)
                    
                    # Captura o percentual de CPU utilizado desde a última checagem
                    cpu_atual = processo.cpu_percent(interval=None)
                    pico_cpu = max(pico_cpu, cpu_atual)
                except:
                    pass
            time.sleep(0.05)  # Intervalo ideal para amostragem de CPU sem travar o laço

        proc.wait()
        fim = time.perf_counter()

        tempos.append(fim - inicio)
        memorias.append(pico_memoria)
        cpus.append(pico_cpu)

        if usar_now:
            time.sleep(0.2)
            tamanho_atual = tamanho_pasta_noworkflow_global(".")
            tamanhos_proveniencia.append(tamanho_atual)

    resultado = {
        "tempo_medio": statistics.mean(tempos),
        "tempo_std": statistics.stdev(tempos) if len(tempos) > 1 else 0,

        "mem_medio": statistics.mean(memorias),
        "mem_std": statistics.stdev(memorias) if len(memorias) > 1 else 0,
        
        "cpu_media_pico": statistics.mean(cpus)  # Média dos picos de CPU observados
    }

    if usar_now:
        resultado["prov_media"] = max(tamanhos_proveniencia) if tamanhos_proveniencia else 0
        resultado["trials"] = EXECUCOES

    return resultado


resultados = []

for script in SCRIPTS:

    print(f"Executando {script}")

    normal = executar(script)
    workflow = executar(script, usar_now=True)

    overhead_tempo = ((workflow["tempo_medio"] - normal["tempo_medio"]) / normal["tempo_medio"]) * 100
    overhead_memoria = ((workflow["mem_medio"] - normal["mem_medio"]) / normal["mem_medio"]) * 100

    cv_normal = (normal["tempo_std"] / normal["tempo_medio"]) * 100
    cv_now = (workflow["tempo_std"] / workflow["tempo_medio"]) * 100

    resultados.append({
        "script": script,

        "tempo_normal": normal["tempo_medio"],
        "tempo_now": workflow["tempo_medio"],

        "mem_normal_mb": normal["mem_medio"] / 1024 / 1024,
        "mem_now_mb": workflow["mem_medio"] / 1024 / 1024,
        
        "cpu_pico_normal_%": normal["cpu_media_pico"],
        "cpu_pico_now_%": workflow["cpu_media_pico"],

        "overhead_tempo_%": overhead_tempo,
        "overhead_memoria_%": overhead_memoria,

        "cv_normal_%": cv_normal,
        "cv_now_%": cv_now,

        "prov_mb": workflow["prov_media"] / 1024 / 1024,
        "trials": workflow["trials"]
    })

df = pd.DataFrame(resultados)
df.to_csv("resultado_experimento.csv", index=False)

# Configuração para exibir todas as colunas no print do terminal
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(df)
