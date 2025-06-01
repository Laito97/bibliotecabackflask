import pandas as pd
from joblib import load

def recomendar_libros_para_usuario(user_id, top_n=5):
    try:
        matrix = load('app/ml/model.pkl')

        if user_id not in matrix.index:
            return []

        # Similaridad entre usuarios (coseno)
        from sklearn.metrics.pairwise import cosine_similarity
        similarities = cosine_similarity([matrix.loc[user_id]], matrix)
        similarities_df = pd.DataFrame(similarities[0], index=matrix.index)

        # Buscar los usuarios más similares
        similares = similarities_df.sort_values(ascending=False).drop(user_id).head(5).index

        # Libros que esos usuarios leyeron y el actual no
        libros_usuario = matrix.loc[user_id]
        libros_leidos = libros_usuario[libros_usuario > 0].index

        recomendaciones = pd.Series(0, index=matrix.columns)
        for u in similares:
            recomendaciones += matrix.loc[u]

        # Eliminar libros ya leídos
        recomendaciones = recomendaciones.drop(libros_leidos, errors='ignore')
        recomendaciones = recomendaciones.sort_values(ascending=False).head(top_n)

        return list(recomendaciones.index)
    except Exception as e:
        print(f"Error al recomendar: {e}")
        return []
