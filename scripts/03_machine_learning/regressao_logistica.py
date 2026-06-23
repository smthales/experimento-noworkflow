from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import time

inicio = time.time()

X, y = load_iris(return_X_y=True)

modelo = LogisticRegression(max_iter=1000)

modelo.fit(X, y)

fim = time.time()

#print("Tempo:", fim - inicio)