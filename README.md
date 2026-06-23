# Avaliação da captura de proveniência em scripts Python com noWorkflow

Este repositório contém a estrutura inicial do experimento desenvolvido para avaliar o impacto do uso do noWorkflow na execução de scripts Python.

O objetivo do trabalho é comparar execuções tradicionais de scripts Python com execuções instrumentadas pelo noWorkflow, analisando principalmente tempo de execução, uso de memória e uso de CPU.

## Ambiente utilizado

O experimento foi configurado em ambiente Linux via WSL.

Versões utilizadas até o momento:

```text
Python 3.12.3
noWorkflow 2.1.1
```

As dependências do ambiente estão registradas no arquivo:

```text
requirements.txt
```

Para recriar o ambiente:

```bash
python3.12 -m venv .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Estrutura do projeto

```text
experimento-noworkflow/
├── data/
├── results/
│   ├── teste_resultados.csv
│   ├── resultados_preliminares.csv
│   └── resumo_preliminar.csv
├── scripts/
│   ├── teste.py
│   ├── numerico.py
│   ├── arquivos.py
│   └── ordenacao.py
├── analisar_resultados.py
├── environment.txt
├── requirements.txt
├── run_experiments.sh
├── run_test.sh
└── README.md
```

## Scripts utilizados

Até o momento, foram preparados três scripts piloto:

| Script         | Categoria                     | Descrição                                                   |
| -------------- | ----------------------------- | ----------------------------------------------------------- |
| `numerico.py`  | Processamento numérico        | Realiza operações com matrizes usando NumPy                 |
| `arquivos.py`  | Leitura e escrita de arquivos | Gera, lê e processa um arquivo CSV                          |
| `ordenacao.py` | Ordenação e busca             | Gera uma lista de números, ordena e realiza buscas binárias |

O arquivo `teste.py` foi utilizado apenas para validação inicial do ambiente e não representa um resultado oficial do experimento.

## Fluxo de execução

O fluxo atual do experimento é:

```text
scripts/*.py
   ↓
run_experiments.sh
   ↓
results/resultados_preliminares.csv
   ↓
analisar_resultados.py
   ↓
results/resumo_preliminar.csv
```

## Execução dos experimentos

O arquivo `run_experiments.sh` automatiza a execução dos scripts piloto.

Para cada script, são realizadas:

* 3 execuções no modo tradicional;
* 3 execuções com noWorkflow.

Com os três scripts atuais, isso gera um total de 18 execuções.

Para executar:

```bash
./run_experiments.sh
```

O resultado bruto é salvo em:

```text
results/resultados_preliminares.csv
```

## Coleta de métricas

As métricas são coletadas com o comando `/usr/bin/time`.

O script de execução utiliza o formato:

```bash
/usr/bin/time -f "%e,%M,%P"
```

Os campos coletados são:

| Campo | Significado                         |
| ----- | ----------------------------------- |
| `%e`  | Tempo real de execução, em segundos |
| `%M`  | Pico de memória residente, em KB    |
| `%P`  | Percentual de CPU utilizado         |

Essas métricas são registradas para cada execução individual.

## Execução tradicional e instrumentada

A execução tradicional é feita com:

```bash
python scripts/nome_do_script.py
```

A execução instrumentada é feita com:

```bash
now run scripts/nome_do_script.py
```

O noWorkflow registra a proveniência das execuções em uma base local `.noworkflow`, que não é versionada no GitHub.

## Análise dos resultados

Após a execução dos experimentos, o arquivo `analisar_resultados.py` processa os dados brutos.

Para executar a análise:

```bash
python analisar_resultados.py
```

Esse script lê:

```text
results/resultados_preliminares.csv
```

E gera:

```text
results/resumo_preliminar.csv
```

O resumo contém as médias das execuções tradicionais e instrumentadas, além do cálculo de overhead de tempo e memória.

## Fórmulas de overhead

O overhead de tempo é calculado por:

```text
overhead_tempo (%) =
((tempo_medio_noworkflow - tempo_medio_tradicional) / tempo_medio_tradicional) × 100
```

O overhead de memória é calculado por:

```text
overhead_memoria (%) =
((memoria_media_noworkflow - memoria_media_tradicional) / memoria_media_tradicional) × 100
```

## Resultados preliminares

Até o momento, os resultados indicam que a execução com noWorkflow aumenta o tempo total de execução e o consumo de memória dos scripts avaliados.

Os resultados consolidados estão disponíveis em:

```text
results/resumo_preliminar.csv
```

Os dados brutos de cada execução estão em:

```text
results/resultados_preliminares.csv
```

## Observações técnicas

Algumas particularidades observadas até o momento:

* Scripts com muitas operações pequenas em Python puro tendem a apresentar overhead maior quando instrumentados.
* Scripts com operações realizadas por bibliotecas otimizadas, como NumPy, tendem a apresentar overhead mais controlado.
* Como alguns scripts possuem tempo tradicional muito baixo, o overhead percentual pode ficar muito alto. Por isso, a análise deve considerar também os tempos absolutos.
* A pasta `.noworkflow` é ignorada pelo Git para evitar versionar a base interna de proveniência.
* Arquivos de dados gerados automaticamente, como `data/dados_arquivos.csv`, também não são versionados.

## Status atual

Até esta etapa, foram concluídos:

* configuração do ambiente;
* instalação e validação do noWorkflow;
* criação dos scripts piloto;
* automatização das execuções;
* coleta dos resultados preliminares;
* geração de resumo com médias e overheads.

Próximos passos:

* adicionar scripts de outras categorias;
* ampliar o conjunto experimental;
* gerar gráficos comparativos;
* aprofundar a análise dos resultados.
