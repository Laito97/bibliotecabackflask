import pandas as pd
from joblib import load

# Cargar la matriz guardada
matrix = load('app/ml/model.pkl')

# Verifica los índices (usuarios)
print(matrix.index.tolist())  # Lista de todos los user_id incluidos
