from app.models.model_categoria import Categoria
from flask import jsonify

class CategoriaService:

    @staticmethod
    def listar_categorias():
        try:
            categorias = Categoria.query.all()
            categorias_data = []

            for categoria in categorias:
                categorias_data.append({
                    'categoria_id': categoria.categoria_id,
                    'categoria_nom': categoria.categoria_nom,
                })

            return jsonify({
                'response_code': 200,
                'message': 'Categorías listadas exitosamente',
                'categorias': categorias_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al listar categorías: {str(e)}'
            }), 500
