from flask import Blueprint
from app.services.autor_service import AutorService  

autor_bp = Blueprint('autor_bp', __name__)
main_root = '/autores'

@autor_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_autores():
    return AutorService.listar_autores()
