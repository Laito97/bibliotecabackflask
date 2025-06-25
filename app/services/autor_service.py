from app.models.model_autor import Autor
from app.database import db
from datetime import datetime
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

    @staticmethod
    def guardar_autor(data):
        try:
            autor_id = data.get('autor_id')
            autor_nom = data.get('autor_nom')
            usuario_id = data.get('usuario_creacion_id')

            if not autor_nom or not usuario_id:
                return jsonify({
                    'response_code': 400,
                    'message': 'Faltan datos requeridos: autor_nom o usuario_id.'
                }), 400

            if autor_id:
                autor = Autor.query.get(autor_id)
                if not autor:
                    return jsonify({'response_code': 404, 'message': 'Autor no encontrado'}), 404

                autor.autor_nom = autor_nom
                autor.fecha_actualizacion = datetime.now()
                autor.usuario_actualizacion_id = usuario_id
                mensaje = 'Autor actualizado exitosamente'
            else:
                autor = Autor(
                    autor_nom=autor_nom,
                    fecha_creacion=datetime.now(),
                    usuario_creacion_id=usuario_id
                )
                db.session.add(autor)
                mensaje = 'Autor creado exitosamente'

            db.session.commit()
            return jsonify({
                'response_code': 200,
                'message': mensaje,
                'autor': {
                    'autor_id': autor.autor_id,
                    'autor_nom': autor.autor_nom
                }
            }), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'response_code': 500,
                'message': f'Error al guardar autor: {str(e)}'
            }), 500
        
    
    @staticmethod
    def eliminar_autor(autor_id, usuario_modificacion_id):

        if not usuario_modificacion_id:
            return jsonify({
                'response_code': 400,
                'message': 'Falta el id del usuario que realiza la modificación.'
            }), 400

        try:
            autor = Autor.query.get(autor_id)

            if not autor:
                return jsonify({
                    'response_code': 404,
                    'message': 'Autor no encontrado'
                }), 404

            autor.estado_id = 2 
            autor.fecha_actualizacion = datetime.now()
            autor.usuario_actualizacion_id = usuario_modificacion_id

            db.session.commit()

            return jsonify({
                'response_code': 200,
                'message': 'Autor eliminado (inactivado) exitosamente'
            }), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'response_code': 500,
                'message': f'Error al eliminar autor: {str(e)}'
            }), 500