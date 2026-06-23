from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
import time

inicio = time.time()

X, y = load_wine(return_X_y=True)

modelo = RandomForestClassifier(
    n_estimators=500
)

modelo.fit(X, y)

fim = time.time()

#print("Tempo:", fim - inicio)