from app.models.model_libro import Libro
from app.models.model_prestamo import Prestamo
from app.services.libro_service import LibroService
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecomendacionService:


    @staticmethod
    def recomendar_libros(id_usuario, top_n=5):
        try:
            prestamos = Prestamo.query.filter_by(usuario_solicita_prestamo=id_usuario).all()
            libros_leidos_ids = [p.libro_id for p in prestamos]

            if not libros_leidos_ids:
                return {'mensaje': 'Este usuario no ha leído ningún libro aún.', 'recomendaciones': []}

            libros = Libro.query.all()

            libros_data = []
            for libro in libros:
                contenido = f"{libro.autor.autor_nom if libro.autor else ''} {libro.categoria.categoria_nom if libro.categoria else ''}"
                libros_data.append({
                    'libro_id': libro.libro_id,
                    'libro': libro,
                    'contenido': contenido
                })

            corpus = [l['contenido'] for l in libros_data]
            tfidf = TfidfVectorizer()
            matriz_tfidf = tfidf.fit_transform(corpus)

            indices_leidos = [i for i, l in enumerate(libros_data) if l['libro_id'] in libros_leidos_ids]
            vectores_leidos = matriz_tfidf[indices_leidos].toarray()
            vector_usuario = vectores_leidos.mean(axis=0).reshape(1, -1)

            similitudes = cosine_similarity(vector_usuario, matriz_tfidf).flatten()

            recomendaciones = []
            for i, l in enumerate(libros_data):
                if l['libro_id'] not in libros_leidos_ids:
                    detalle_libro = LibroService.formatear_libro(l['libro'])
                    detalle_libro['similitud'] = round(float(similitudes[i]), 4)
                    recomendaciones.append(detalle_libro)

            recomendaciones.sort(key=lambda x: x['similitud'], reverse=True)

            return {'mensaje': 'Recomendaciones generadas', 'recomendaciones': recomendaciones[:top_n]}

        except Exception as e:
            return {'error': str(e)}
