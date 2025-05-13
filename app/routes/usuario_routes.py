from flask import Blueprint
from app.services.usuario_service import UsuarioService  

usuario_bp = Blueprint('usuario_bp', __name__)
main_root = '/usuarios'

@usuario_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_usuarios():
    return UsuarioService.listar_usuarios()
