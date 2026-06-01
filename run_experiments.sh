#!/bin/bash

mkdir -p results

ARQUIVO_RESULTADOS="results/resultados_preliminares.csv"

echo "script,categoria,modo,execucao,tempo_real_seg,memoria_kb,cpu_percentual" > "$ARQUIVO_RESULTADOS"

executar_tradicional() {
  script=$1
  categoria=$2

  for i in 1 2 3
  do
    /usr/bin/time -f "$script,$categoria,tradicional,$i,%e,%M,%P" \
      -o "$ARQUIVO_RESULTADOS" -a \
      python "scripts/$script" > /dev/null
  done
}

executar_noworkflow() {
  script=$1
  categoria=$2

  for i in 1 2 3
  do
    /usr/bin/time -f "$script,$categoria,noworkflow,$i,%e,%M,%P" \
      -o "$ARQUIVO_RESULTADOS" -a \
      now run "scripts/$script" > /dev/null
  done
}

executar_tradicional "numerico.py" "Processamento numerico"
executar_noworkflow "numerico.py" "Processamento numerico"

executar_tradicional "arquivos.py" "Leitura e escrita de arquivos"
executar_noworkflow "arquivos.py" "Leitura e escrita de arquivos"

executar_tradicional "ordenacao.py" "Ordenacao e busca"
executar_noworkflow "ordenacao.py" "Ordenacao e busca"

echo "Experimentos concluídos. Resultados salvos em $ARQUIVO_RESULTADOS"
