from sklearn.datasets import load_breast_cancer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import time

inicio = time.time()

X, y = load_breast_cancer(return_X_y=True)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("svc", SVC())
])

pipe.fit(X, y)

fim = time.time()

#print("Tempo:", fim - inicio)