from flask import Blueprint
from app.services.prestamo_service import PrestamoService

prestamo_bp = Blueprint('prestamo_bp', __name__)
main_root = '/prestamos'

@prestamo_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_prestamos():
    return PrestamoService.listar_prestamos()
