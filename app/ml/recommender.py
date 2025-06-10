import pandas as pd
from joblib import load
from sklearn.metrics.pairwise import cosine_similarity

def recomendar_libros_para_usuario(user_id, top_n=5):
    try:
        print("Cargando modelo...")
        matrix = load('app/ml/model.pkl')
        print("Modelo cargado.")

        if user_id not in matrix.index:
            print("Usuario no está en la matriz.")
            return []

        print("Calculando similitud...")
        user_vector = matrix.loc[[user_id]]
        similarities = cosine_similarity(user_vector, matrix)

        similarities_series = pd.Series(similarities[0], index=matrix.index)
        print("Similitudes calculadas.")

        similares = similarities_series.sort_values(ascending=False).drop(user_id).head(5).index
        print(f"Usuarios similares: {list(similares)}")

        libros_usuario = matrix.loc[user_id]
        libros_leidos = libros_usuario[libros_usuario > 0].index
        print(f"Libros ya leídos: {list(libros_leidos)}")

        recomendaciones = pd.Series(0.0, index=matrix.columns)
        for u in similares:
            recomendaciones = recomendaciones.add(matrix.loc[u], fill_value=0)

        recomendaciones = recomendaciones.drop(libros_leidos, errors='ignore')
        recomendaciones = recomendaciones.sort_values(ascending=False).head(top_n)

        print(f"Recomendaciones: {list(recomendaciones.index)}")
        return list(recomendaciones.index)

    except Exception as e:
        print(f"Error al recomendar: {e}")
        return []

