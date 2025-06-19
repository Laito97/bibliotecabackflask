from flask import Blueprint, jsonify
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import traceback

recomendaciones_bp = Blueprint("recomendaciones_bp", __name__)
main_root = '/recomendaciones'

# Aislar error de importación
try:
    from app.services.recomendaciones_service import RecomendacionesService
    from app.ml.recomendaciones_training_model import entrenar_modelo
    from app.resource.recomendaciones_resource import recomendar_libros
    print("[INFO] Todos los módulos importados correctamente")
except Exception as e:
    print("[FATAL] Error al importar módulos:")
    traceback.print_exc()

@recomendaciones_bp.route(f'{main_root}/test', methods=["GET"])
def test_ok():
    return jsonify({"message": "funciona"})

@recomendaciones_bp.route(f'{main_root}/test-sklearn', methods=["GET"])
def test_sklearn():
    try:
        A = np.array([[1, 0], [0, 1]])
        sim = cosine_similarity(A)
        return jsonify(similarity=sim.tolist())
    except Exception as e:
        print("[ERROR] test sklearn")
        traceback.print_exc()
        return jsonify({"error": "Error interno"}), 500
