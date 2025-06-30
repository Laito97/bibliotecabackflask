from app.models.model_prestamo import Prestamo
from flask import jsonify
from app import db
from datetime import datetime
from flask import request

class PrestamoService:

    @staticmethod
    def listar_prestamos():
        try:
            prestamos = Prestamo.query.all()
            prestamos_data = []

            for prestamo in prestamos:
                prestamos_data.append({
                    'prestamo_id': prestamo.prestamo_id,
                    'libro': {
                        'libro_id': prestamo.libro.libro_id,
                        'libro_nom': prestamo.libro.libro_nom,
                        'isbn': prestamo.libro.isbn
                    },
                    'usuario_solicita_prestamo': {
                        'usuario_id': prestamo.usuario_solicita.usuario_id,
                        'usuario_nombre': prestamo.usuario_solicita.usu_nom
                    },
                    'usuario_aprueba_prestamo': {
                        'usuario_id': prestamo.usuario_aprueba.usuario_id,
                        'usuario_nombre': prestamo.usuario_aprueba.usu_nom
                    },
                    'fecha_solicitud_prestamo': prestamo.fecha_solicitud_prestamo.strftime('%Y-%m-%d %H:%M:%S'),
                    'fecha_devolucion_prestamo': prestamo.fecha_devolucion_prestamo.strftime('%Y-%m-%d %H:%M:%S') if prestamo.fecha_devolucion_prestamo else None,
                    'prestamo_estado': {
                        'estado_id': prestamo.prestamo_estado.prestamo_estado_id,
                        'estado_nombre': prestamo.prestamo_estado.descripcion
                    },
                    'fecha_creacion': prestamo.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
                    'usuario_creacion_id': prestamo.usuario_creacion_id,
                    'fecha_actualizacion': prestamo.fecha_actualizacion.strftime('%Y-%m-%d %H:%M:%S') if prestamo.fecha_actualizacion else None,
                    'usuario_actualizacion_id': prestamo.usuario_actualizacion_id
                })

            return jsonify({
                'response_code': 200,
                'message': 'Préstamos listados exitosamente',
                'prestamos': prestamos_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al listar préstamos: {str(e)}'
            }), 500


    @staticmethod
    def guardar_editar_prestamo():
        try:
            data = request.get_json()
            now = datetime.now()

            prestamo_id = data.get('prestamo_id')
            prestamo = None

            if prestamo_id:
                prestamo = Prestamo.query.get(prestamo_id)
                if not prestamo:
                    return jsonify({'response_code': 404, 'message': 'Préstamo no encontrado'}), 404
                prestamo.fecha_actualizacion = now
                prestamo.usuario_actualizacion_id = data.get('usuario_actualizacion_id')
            else:
                prestamo = Prestamo(
                    fecha_creacion=now,
                    usuario_creacion_id=data.get('usuario_creacion_id')
                )
                db.session.add(prestamo)

            prestamo.libro_id = data.get('libro_id')
            prestamo.usuario_solicita_prestamo = data.get('usuario_solicita_prestamo')
            prestamo.usuario_aprueba_prestamo = data.get('usuario_aprueba_prestamo')
            
            fecha_solicitud_str = data.get('fecha_solicitud_prestamo')
            if fecha_solicitud_str:
                prestamo.fecha_solicitud_prestamo = datetime.strptime(fecha_solicitud_str, '%Y-%m-%d %H:%M:%S')

            fecha_devolucion_str = data.get('fecha_devolucion_prestamo')
            if fecha_devolucion_str:
                prestamo.fecha_devolucion_prestamo = datetime.strptime(fecha_devolucion_str, '%Y-%m-%d %H:%M:%S')
            else:
                prestamo.fecha_devolucion_prestamo = None

            prestamo.prestamo_estado_id = data.get('prestamo_estado_id')

            db.session.commit()

            return jsonify({
                'response_code': 200,
                'message': 'Préstamo actualizado exitosamente' if prestamo_id else 'Préstamo creado exitosamente',
                'prestamo_id': prestamo.prestamo_id
            }), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'response_code': 500,
                'message': f'Error al guardar/editar préstamo: {str(e)}'
            }), 500
<<<<<<< HEAD
=======
        
>>>>>>> 9525f9dd2aaa0e57a4e2a6e28fc3e263e20ee57c
    @staticmethod
    def eliminar_prestamo(prestamo_id, usuario_modificacion_id):

        if not usuario_modificacion_id:
            return jsonify({
                'response_code': 400,
                'message': 'Falta el id del usuario que realiza la modificación.'
            }), 400

        try:
            prestamo = Prestamo.query.get(prestamo_id)

            if not prestamo:
                return jsonify({
                    'response_code': 404,
                    'message': 'Prestamo no encontrado'
                }), 404

            prestamo.estado_id = 2 
            prestamo.fecha_actualizacion = datetime.now()
            prestamo.usuario_actualizacion_id = usuario_modificacion_id

            db.session.commit()

            return jsonify({
                'response_code': 200,
                'message': 'Prestamo eliminado exitosamente'
            }), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'response_code': 500,
                'message': f'Error al eliminar prestamo: {str(e)}'
            }), 500