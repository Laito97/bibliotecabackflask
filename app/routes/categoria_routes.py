from flask import Blueprint
from app.services.categoria_service import CategoriaService  

categoria_bp = Blueprint('categoria_bp', __name__)
main_root = '/categorias'

@categoria_bp.route(f'{main_root}/list', methods=['GET'])
def obtener_categoria():
    return CategoriaService.listar_categorias()
