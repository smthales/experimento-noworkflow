import pandas as pd
import numpy as np
import time

inicio = time.time()

# Gerar dados simulados
np.random.seed(42)

df = pd.DataFrame({
    "idade": np.random.randint(18, 70, 100000),
    "salario": np.random.normal(5000, 1500, 100000),
    "anos_experiencia": np.random.randint(0, 40, 100000)
})

# Estatísticas descritivas
estatisticas = df.describe()

# Correlação
correlacao = df.corr()

#print("Estatísticas:")
#print(estatisticas)

#print("\nCorrelação:")
#print(correlacao)

fim = time.time()

#print(f"\nTempo de execução: {fim - inicio:.4f} segundos")