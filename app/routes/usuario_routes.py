from flask import Blueprint
from flask import request
from app.services.usuario_service import UsuarioService  

usuario_bp = Blueprint('usuario_bp', __name__)
main_root = '/usuarios'

@usuario_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_usuarios():
    return UsuarioService.listar_usuarios()

@usuario_bp.route(f'{main_root}/guardar', methods=['POST'])
def guardar_usuario():
    data = request.get_json()
    return UsuarioService.guardar_usuario(data)

@usuario_bp.route(f'{main_root}/list-tipo', methods=['GET'])
def obtener_usuario_tipo():
    return UsuarioService.listar_usuario_tipo()