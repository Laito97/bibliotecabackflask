from app.models.model_autor import Autor
from flask import jsonify

class AutorService:

    @staticmethod
    def listar_autores():
        try:
            autores = Autor.query.all()
            autores_data = []

            for autor in autores:
                autores_data.append({
                    'autor_id': autor.autor_id,
                    'autor_nom': autor.autor_nom,
                    'fecha_creacion': autor.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S') if autor.fecha_creacion else None,
                    'usuario_creacion_id': autor.usuario_creacion_id,
                    'fecha_actualizacion': autor.fecha_actualizacion.strftime('%Y-%m-%d %H:%M:%S') if autor.fecha_actualizacion else None,
                    'usuario_actualizacion_id': autor.usuario_actualizacion_id
                })

            return jsonify({
                'response_code': 200,
                'message': 'Autores listados exitosamente',
                'autores': autores_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al listar autores: {str(e)}'
            }), 500
