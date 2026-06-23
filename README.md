# experimento-noworkflow

Trabalho final da disciplina **eScience 2026.1** — avaliação da captura de proveniência em scripts Python, comparando execuções tradicionais e instrumentadas com o [noWorkflow](https://github.com/gems-uff/noworkflow).

**Autores:** Elvis Souza de Oliveira Junior, Paulo Mauricio de Souza Mota e Thales de Souza Machado Abranches do Nascimento.

## Sobre o trabalho

Este repositório contém o experimento desenvolvido para responder à seguinte questão central:

> Qual o impacto do uso do noWorkflow no desempenho de scripts Python, comparando execuções tradicionais e instrumentadas?

O estudo avalia o **overhead** introduzido pela captura automática de proveniência em diferentes categorias de aplicação, considerando as métricas:

- **Tempo de execução** — duração total de cada script
- **Uso de memória RAM** — pico de consumo durante a execução
- **Uso de CPU** — percentual de utilização do processador
- **Volume de proveniência** — tamanho dos metadados gerados pelo noWorkflow em disco

### Questões de pesquisa

1. Qual o impacto do noWorkflow no tempo de execução?
2. Qual o impacto no consumo de memória?
3. O overhead varia conforme a natureza da aplicação?
4. Qual o custo da captura de proveniência gerada?

### Metodologia

Foram selecionados **12 scripts** de naturezas distintas, executados em **dois cenários** (com e sem noWorkflow), com **3 repetições** por cenário — totalizando **72 execuções**.

| Categoria | Recurso principal | Scripts |
|-----------|-------------------|---------|
| Computação numérica | CPU | `soma_de_quadrados.py`, `numeros_primos.py` |
| Manipulação de dados (pandas) | CPU + Memória | `filtragem.py`, `agrupamento.py` |
| Machine Learning | CPU + Memória | `regressao_logistica.py`, `random_forest.py` |
| Manipulação de arquivos (I/O) | I/O | `escrita.py`, `leitura.py` |
| Pipeline de ML | CPU + Memória | `normalizacao_mais_treino.py`, `pipeline_completo.py` |
| Ciência de dados | CPU + Memória | `analise_exploratoria_dados.py`, `limpeza_transformacao_de_dados.py` |

## Estrutura do repositório

```
experimento-noworkflow/
└── scripts/
    ├── 01_matematica/
    ├── 02_manipulacao_de_dados_pandas/
    ├── 03_machine_learning/
    ├── 04_arquivos/
    ├── 05_pipeline_ml/
    ├── 06_analise_de_dados/
    ├── benchmark_academico_v2.py
    └── resultado_experimento.csv   ← gerado após a execução
```

## Pré-requisitos

- Python 3
- [noWorkflow](https://github.com/gems-uff/noworkflow) instalado e configurado (`now` disponível no PATH)
- Dependências Python:

```bash
pip install pandas psutil
```

## Como executar

Entre na pasta `scripts` e execute o benchmark:

```bash
cd scripts
python3 benchmark_academico_v2.py
```

O script irá:

1. Executar cada um dos 12 scripts no modo **tradicional** (`python3`)
2. Executar cada script novamente com **noWorkflow** (`now run`)
3. Repetir cada cenário **3 vezes**
4. Coletar tempo, memória, CPU e volume de proveniência
5. Calcular o overhead entre os dois modos

Ao final, será gerado o arquivo **`resultado_experimento.csv`** na pasta `scripts/`, contendo os resultados consolidados de todas as execuções.

### Executar um script individualmente

**Sem noWorkflow:**

```bash
python3 01_matematica/numeros_primos.py
```

**Com noWorkflow:**

```bash
now run 01_matematica/numeros_primos.py
```

## Resultados esperados

O arquivo `resultado_experimento.csv` contém, para cada script:

| Coluna | Descrição |
|--------|-----------|
| `script` | Caminho do script avaliado |
| `tempo_normal` / `tempo_now` | Tempo médio de execução (s) |
| `mem_normal_mb` / `mem_now_mb` | Pico de memória (MB) |
| `cpu_pico_normal_%` / `cpu_pico_now_%` | Pico de CPU (%) |
| `overhead_tempo_%` | Aumento percentual no tempo |
| `overhead_memoria_%` | Aumento percentual na memória |
| `prov_mb` | Volume de proveniência gerado (MB) |

## Repositório

https://github.com/smthales/experimento-noworkflow
