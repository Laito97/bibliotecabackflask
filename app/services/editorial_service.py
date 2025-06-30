from app.models.model_editorial import Editorial
from flask import jsonify
from app.database import db
from datetime import datetime


class EditorialService:

    @staticmethod
    def listar_editoriales():
        try:
            editoriales = Editorial.query.filter_by(estado_id=1).all()
            editoriales_data = []

            for editorial in editoriales:
                editoriales_data.append({
                    'editorial_id': editorial.editorial_id,
                    'editorial_nom': editorial.editorial_nom,
                })

            return jsonify({
                'response_code': 200,
                'message': 'Editoriales listadas exitosamente',
                'editoriales': editoriales_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al listar editoriales: {str(e)}'
            }), 500
        
    @staticmethod
    def guardar_editar_editorial(data):
        try:
            nombre = data.get('editorial_nom')
            editorial_id = data.get('editorial_id')

            if not nombre:
                return jsonify({
                    'response_code': 400,
                    'message': 'El nombre de la editorial es obligatorio.'
                }), 400

            if editorial_id:
                editorial = Editorial.query.get(editorial_id)
                if not editorial:
                    return jsonify({
                        'response_code': 404,
                        'message': 'Editorial no encontrada.'
                    }), 404

                editorial.editorial_nom = nombre
                db.session.commit()

                return jsonify({
                    'response_code': 200,
                    'message': 'Editorial actualizada exitosamente.',
                    'editorial': {
                        'editorial_id': editorial.editorial_id,
                        'editorial_nom': editorial.editorial_nom
                    }
                }), 200

            nueva_editorial = Editorial(editorial_nom=nombre)
            db.session.add(nueva_editorial)
            db.session.commit()

            return jsonify({
                'response_code': 201,
                'message': 'Editorial guardada exitosamente.',
                'editorial': {
                    'editorial_id': nueva_editorial.editorial_id,
                    'editorial_nom': nueva_editorial.editorial_nom
                }
            }), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'response_code': 500,
                'message': f'Error al guardar o editar editorial: {str(e)}'
            }), 500

    @staticmethod
    def eliminar_editorial(editorial_id, usuario_modificacion_id):

        if not usuario_modificacion_id:
            return jsonify({
                'response_code': 400,
                'message': 'Falta el id del usuario que realiza la modificación.'
            }), 400

        try:
            editorial = Editorial.query.get(editorial_id)

            if not editorial:
                return jsonify({
                    'response_code': 404,
                    'message': 'Editorial no encontrado'
                }), 404

            editorial.estado_id = 2 
            editorial.fecha_actualizacion = datetime.now()
            editorial.usuario_actualizacion_id = usuario_modificacion_id

            db.session.commit()

            return jsonify({
                'response_code': 200,
                'message': 'Editorial eliminada exitosamente'
            }), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'response_code': 500,
                'message': f'Error al eliminar editorial: {str(e)}'
            }), 500