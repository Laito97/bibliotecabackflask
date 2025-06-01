# app/routes/recomendacion_routes.py
from flask import Blueprint, jsonify
from app.ml.recommender import recomendar_libros_para_usuario
from app.models.model_libro import Libro

recomendaciones_bp = Blueprint('recomendaciones', __name__)

@recomendaciones_bp.route('/recomendaciones/<int:user_id>', methods=['GET'])
def recomendaciones(user_id):
    ids = recomendar_libros_para_usuario(user_id)
    libros = Libro.query.filter(Libro.libro_id.in_(ids)).all()
    return jsonify([libro.to_dict() for libro in libros])