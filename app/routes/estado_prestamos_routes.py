from flask import Blueprint
from flask import request
from app.services.prestamo_estado_service import PrestamoEstadoService

estado_prestamos_bp = Blueprint('prestamo_estado_bp', __name__)
main_root = '/prestamo-estado'

@estado_prestamos_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_estados():
    return PrestamoEstadoService.listar_estados_prestamo()

