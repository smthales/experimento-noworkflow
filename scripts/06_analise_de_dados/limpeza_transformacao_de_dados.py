import pandas as pd
import numpy as np
import time

inicio = time.time()

# Dados simulados com valores ausentes
np.random.seed(42)

df = pd.DataFrame({
    "idade": np.random.randint(18, 70, 50000),
    "salario": np.random.normal(5000, 1500, 50000),
    "cidade": np.random.choice(
        ["Rio", "São Paulo", "Belo Horizonte"],
        50000
    )
})

# Inserir valores ausentes
df.loc[df.sample(frac=0.1).index, "salario"] = np.nan

# Limpeza
df["salario"] = df["salario"].fillna(
    df["salario"].mean()
)

# Transformação categórica
df = pd.get_dummies(
    df,
    columns=["cidade"]
)

# Normalização
df["salario"] = (
    df["salario"] - df["salario"].mean()
) / df["salario"].std()

#print(df.head())

fim = time.time()

#print(f"\nTempo de execução: {fim - inicio:.4f} segundos")