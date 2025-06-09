from flask import Blueprint
from flask import request
from app.services.libro_service import LibroService

libro_bp = Blueprint('libro_bp', __name__)
main_root = '/libros'

@libro_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_libros():
    return LibroService.listar_libros()

@libro_bp.route(f'{main_root}/save-update', methods=['POST'])
def guardar_o_editar_libro():
    data = request.get_json()
    return LibroService.guardar_editar_libro(data)
