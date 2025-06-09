from flask import Blueprint
from flask import request
from app.services.autor_service import AutorService  

autor_bp = Blueprint('autor_bp', __name__)
main_root = '/autores'

@autor_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_autores():
    return AutorService.listar_autores()

@autor_bp.route(f'{main_root}/save-update', methods=['POST'])
def guardar_autor():
    data = request.get_json()
    return AutorService.guardar_autor(data)