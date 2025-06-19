
print("Cargando: recomendaciones_training_model")


def recomendar_libros(usuario_id, user_book_matrix, similarity_df, top_n=5):
    if usuario_id not in similarity_df.index:
        return []  # Usuario nuevo sin historial

    # Buscar los usuarios más similares
    similares = similarity_df[usuario_id].sort_values(ascending=False)[1:]  # excluye a sí mismo

    # Sumar puntuaciones ponderadas por similitud
    recomendacion_scores = user_book_matrix.T.dot(similares)

    # Filtrar libros que el usuario ya leyó
    libros_leidos = user_book_matrix.loc[usuario_id]
    libros_no_leidos = libros_leidos[libros_leidos == 0]

    # Seleccionar recomendaciones de libros no leídos
    recomendaciones = recomendacion_scores[libros_no_leidos.index]
    recomendaciones = recomendaciones.sort_values(ascending=False).head(top_n)

    return list(recomendaciones.index)
