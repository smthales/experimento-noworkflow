from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import time

inicio = time.time()

X, y = load_wine(return_X_y=True)

X = StandardScaler().fit_transform(X)

modelo = RandomForestClassifier(
    n_estimators=200
)

modelo.fit(X, y)

fim = time.time()

#print("Tempo:", fim - inicio)