from flask import Blueprint
from app.services.libro_service import LibroService

libro_bp = Blueprint('libro_bp', __name__)
main_root = '/libros'

@libro_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_libros():
    return LibroService.listar_libros()
