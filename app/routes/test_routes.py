from flask import Blueprint, jsonify, request
import tensorflow as tf
import numpy as np
from app.services.recomendacion_service import RecomendacionService
from app.models.model_libro import Libro
from app.services.libro_service import LibroService
import pandas as pd

test_bp = Blueprint("test_bp", __name__)
main_root = '/test'

modelo = tf.keras.models.load_model('E:\\nueva version\\biblioteca-backend-flask\\modelo_temperatura.h5')
modelo_recomendacion  = tf.keras.models.load_model('E:\\nueva version\\biblioteca-backend-flask\\modelo_temperatura.h5')
print("Modelo cargado desde modelo tal")

@test_bp.route(f'{main_root}', methods=['GET'])
def test_ok():
    celsius = 30
    input_data = np.array([[celsius]], dtype=np.float32)
    prediction = modelo.predict(input_data)
    fahrenheit_value = float(prediction[0][0])

    response = {
        'celsius': celsius,
        'fahrenheit': fahrenheit_value
    }

    return jsonify(response)

@test_bp.route(f'{main_root}/predecir_temperatura', methods=['POST'])
def predecir_temperatura():
    try:
        data = request.json
        dia = data.get('dia')

        if dia is None:
            return jsonify({'error': 'Se requiere el valor "dia" en el cuerpo de la solicitud'}), 400

        # Convertir a numpy y hacer la predicción
        dia_array = np.array([float(dia)])
        prediccion = modelo.predict(dia_array)[0][0]

        return jsonify({
            'dia': dia,
            'prediccion_temperatura': round(float(prediccion), 2)  # Conversión explícita
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@test_bp.route(f'{main_root}/recomendar', methods=['POST'])
def recomendar():
    try:
        data = request.get_json()
        id_usuario = data.get('id_usuario')

        if not id_usuario:
            return jsonify({'response_code': 400, 'message': 'Se requiere id_usuario'}), 400

        resultado = RecomendacionService.recomendar_libros(id_usuario)

        return jsonify({
            'response_code': 200,
            'message': resultado.get('mensaje', ''),
            'recomendaciones': resultado.get('recomendaciones', [])
        }), 200

    except Exception as e:
        return jsonify({'response_code': 500, 'message': f'Error: {str(e)}'}), 500


@test_bp.route(f'{main_root}/recomendar2', methods=['POST'])
def recomendar2():
    try:
        data = request.get_json()
        id_usuario = data.get('id_usuario')

        if not id_usuario:
            return jsonify({'response_code': 400, 'message': 'Se requiere id_usuario'}), 400

        # Ruta del archivo de recomendaciones
        ruta_h5 = f'C:\\proyectolaito\\bibliotecabackflask\\recomendaciones_usuario_1.h5'

        # Cargar el archivo h5 con pandas
        df = pd.read_hdf(ruta_h5)

        # Convertir DataFrame a lista de diccionarios
        recomendaciones = df.to_dict(orient='records')

        return jsonify({
            'response_code': 200,
            'message': 'Recomendaciones generadas',
            'recomendaciones': recomendaciones
        }), 200

    except FileNotFoundError:
        return jsonify({'response_code': 404, 'message': 'No se encontraron recomendaciones para este usuario'}), 404
    except Exception as e:
        return jsonify({'response_code': 500, 'message': f'Error: {str(e)}'}), 500