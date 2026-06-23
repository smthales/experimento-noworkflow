import pandas as pd
import numpy as np
import time

inicio = time.time()

df = pd.DataFrame({
    "idade": np.random.randint(18, 80, 200000),
    "salario": np.random.randint(1000, 10000, 200000)
})

resultado = df[df["idade"] > 40]

fim = time.time()

#print(resultado.shape)
#print("Tempo:", fim - inicio)