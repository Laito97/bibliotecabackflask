from app.models.model_prestamo import Prestamo
from flask import jsonify

class PrestamoService:

    @staticmethod
    def listar_prestamos():
        try:
            # Usamos `joinedload` para cargar relaciones de manera eficiente
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
