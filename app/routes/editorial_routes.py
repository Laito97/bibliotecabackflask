from flask import Blueprint
from flask import request
from app.services.editorial_service import EditorialService  

editorial_bp = Blueprint('editorial_bp', __name__)
main_root = '/editoriales'

@editorial_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_editoriales():
    return EditorialService.listar_editoriales()

@editorial_bp.route(f'{main_root}/save-update', methods=['POST'])
def guardar_o_editar_editorial():
    data = request.get_json()
    return EditorialService.guardar_editar_editorial(data)
