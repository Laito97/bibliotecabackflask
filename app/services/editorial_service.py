from app.models.model_editorial import Editorial
from flask import jsonify

class EditorialService:

    @staticmethod
    def listar_editoriales():
        try:
            editoriales = Editorial.query.all()
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
