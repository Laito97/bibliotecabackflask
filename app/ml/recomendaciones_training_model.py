from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
import pandas as pd
print("Cargando: recomendaciones_training_model")


def entrenar_modelo(df):
    # Creamos la matriz usuario-libro
    user_book_matrix = df.pivot_table(index='usuario_id', columns='libro_id', aggfunc=len, fill_value=0)

    # Convertimos a matriz dispersa
    sparse_matrix = csr_matrix(user_book_matrix.values)

    # Calculamos similitud entre usuarios
    user_similarity = cosine_similarity(sparse_matrix)

    # Creamos un DataFrame de similitud
    similarity_df = pd.DataFrame(user_similarity, index=user_book_matrix.index, columns=user_book_matrix.index)

    print(user_book_matrix.head())

    return user_book_matrix, similarity_df
