<<<<<<< HEAD
from flask import Blueprint, request
=======
from flask import Blueprint
from flask import request
>>>>>>> 9525f9dd2aaa0e57a4e2a6e28fc3e263e20ee57c
from app.services.prestamo_service import PrestamoService

prestamo_bp = Blueprint('prestamo_bp', __name__)
main_root = '/prestamos'

@prestamo_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_prestamos():
    return PrestamoService.listar_prestamos()

@prestamo_bp.route(f'{main_root}/save-update', methods=['POST'])
def guardar_editar_prestamo():
    return PrestamoService.guardar_editar_prestamo()
<<<<<<< HEAD
=======

>>>>>>> 9525f9dd2aaa0e57a4e2a6e28fc3e263e20ee57c
@prestamo_bp.route(f'{main_root}/eliminar/<int:prestamo_id>', methods=['PUT'])
def eliminar_prestamo(prestamo_id):
    data = request.get_json()
    usuario_prestamo_id = data.get('usuario_modificacion_id')
<<<<<<< HEAD
    return PrestamoService.eliminar_prestamo(prestamo_id, usuario_prestamo_id)
=======
    return PrestamoService.eliminar_prestamo(prestamo_id, usuario_prestamo_id)
>>>>>>> 9525f9dd2aaa0e57a4e2a6e28fc3e263e20ee57c
