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

@usuario_bp.route(f'{main_root}/<int:usuario_id>', methods=['GET'])
def obtener_usuario_por_id(usuario_id):
    return UsuarioService.listar_usuario_by_id(usuario_id)

@usuario_bp.route(f'{main_root}/list-tipo', methods=['GET'])
def obtener_usuario_tipo():
    return UsuarioService.listar_usuario_tipo()

@usuario_bp.route(f'{main_root}/eliminar/<int:usuario_id>', methods=['PUT'])
def eliminar_usuario(usuario_id):
    data = request.get_json()
    usuario_modificacion_id = data.get('usuario_modificacion_id')
    return UsuarioService.eliminar_usuario(usuario_id, usuario_modificacion_id)