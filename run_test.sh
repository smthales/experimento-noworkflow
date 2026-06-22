#!/bin/bash
mkdir -p results

echo "script,categoria,modo,execucao,tempo_real_seg,memoria_kb,cpu_percentual" > results/teste_resultados.csv

for i in 1 2 3
do
  /usr/bin/time -f "teste.py,Validação,tradicional,$i,%e,%M,%P" \
  -o results/teste_resultados.csv -a \
  python scripts/teste.py > /dev/null
done

for i in 1 2 3
do
  /usr/bin/time -f "teste.py,Validação,noworkflow,$i,%e,%M,%P" \
  -o results/teste_resultados.csv -a \
  now run scripts/teste.py > /dev/null
done
