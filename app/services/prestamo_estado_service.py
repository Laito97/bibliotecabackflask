from flask import jsonify
from app.models.model_prestamo_estado import PrestamoEstado  # ajusta el import si el archivo se llama diferente
from app import db

class PrestamoEstadoService:

    @staticmethod
    def listar_estados_prestamo():
        try:
            estados = PrestamoEstado.query.all()
            estados_data = []

            for estado in estados:
                estados_data.append({
                    'prestamo_estado_id': estado.prestamo_estado_id,
                    'descripcion': estado.descripcion
                })

            return jsonify({
                'response_code': 200,
                'message': 'Estados de préstamo listados exitosamente',
                'estados': estados_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al listar estados de préstamo: {str(e)}'
            }), 500
