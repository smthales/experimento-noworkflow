import pandas as pd
import numpy as np
import time

inicio = time.time()

df = pd.DataFrame({
    "grupo": np.random.randint(1, 100, 500000),
    "valor": np.random.rand(500000)
})

resultado = df.groupby("grupo")["valor"].mean()

fim = time.time()

#print(resultado.head())
#print("Tempo:", fim - inicio)