from flask import jsonify, request
from app.models.model_libro import Libro
from app import db
from datetime import datetime

class LibroService:

    @staticmethod
    def listar_libros():
        try:
            libros = Libro.query.all()
            libros_data = []

            for libro in libros:
                libros_data.append({
                    'libro_id': libro.libro_id,
                    'isbn': libro.isbn,
                    'url_portada': libro.url_portada,
                    'libro_nom': libro.libro_nom,
                    'descripcion': libro.descripcion,
                    'anio_publicacion': libro.anio_publicacion,
                    'edicion': libro.edicion,
                    'existencias': libro.existencias,

                    'categoria': {
                        'categoria_id': libro.categoria.categoria_id if libro.categoria else None,
                        'categoria_nom': libro.categoria.categoria_nom if libro.categoria else None
                    },

                    'editorial': {
                        'editorial_id': libro.editorial.editorial_id if libro.editorial else None,
                        'editorial_nom': libro.editorial.editorial_nom if libro.editorial else None
                    },

                    'autor': {
                        'autor_id': libro.autor.autor_id if libro.autor else None,
                        'autor_nom': libro.autor.autor_nom if libro.autor else None
                    },
                    'usuario_creacion_id': libro.usuario_creacion_id,
                    'usuario_actualizacion_id': libro.usuario_actualizacion_id,
                    'fecha_creacion': libro.fecha_creacion,
                    'fecha_actualizacion': libro.fecha_actualizacion
                })

            return jsonify({
                'response_code': 200,
                'message': 'Libros listados exitosamente',
                'libros': libros_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al listar libros: {str(e)}'
            }), 500


    @staticmethod
    def crear_libro():
        try:
            data = request.json

            nuevo_libro = Libro(
                isbn=data.get('isbn'),
                url_portada=data.get('url_portada'),
                libro_nom=data.get('libro_nom'),
                descripcion=data.get('descripcion'),
                anio_publicacion=data.get('anio_publicacion'),
                edicion=data.get('edicion'),
                existencias=data.get('existencias'),
                categoria_id=data.get('categoria_id'),
                editorial_id=data.get('editorial_id'),
                autor_id=data.get('autor_id'),
                fecha_creacion=datetime.utcnow(),
                usuario_creacion_id=data.get('usuario_creacion_id'),
                fecha_actualizacion=datetime.utcnow(),
                usuario_actualizacion_id=data.get('usuario_actualizacion_id')
            )

            db.session.add(nuevo_libro)
            db.session.commit()

            return jsonify({
                'response_code': 201,
                'message': 'Libro creado exitosamente'
            }), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'response_code': 500,
                'message': f'Error al crear libro: {str(e)}'
            }), 500
