from flask import Blueprint, request, jsonify
from app.models.model_usuario import Usuario
from app.database import db
from flask_jwt_extended import create_access_token
from datetime import timedelta
from werkzeug.security import check_password_hash 

auth_bp = Blueprint('auth', __name__)
main_root = '/auth'

@auth_bp.route(f'{main_root}/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({
            'response_code': 400,
            'message': 'Usuario y contraseña son requeridos'
        }), 400

    usuario = Usuario.query.filter_by(usu_nom=username).first()

    # check_password_hash para validar contraseñas hasheadas
    if not usuario or not check_password_hash(usuario.usu_pass, password):
        return jsonify({
            'response_code': 401,
            'message': 'Credenciales inválidas'
        }), 401

    token = create_access_token(identity=usuario.usuario_id, expires_delta=timedelta(hours=1))

    persona = usuario.persona
    usuario_tipo = usuario.usuario_tipo 

    usuario_data = {
        'usuario_id': usuario.usuario_id,
        'nombre': usuario.usu_nom,
        'correo': persona.correo if persona else None,
        'usuario_tipo': {
            'id': usuario_tipo.usuario_tipo_id,
            'nombre': usuario_tipo.tipo_nom
        } if usuario_tipo else None,
        'persona': {
            'id': persona.persona_id,
            'nombres': persona.nombres,
            'apellidos': persona.apellidos,
            'dni': persona.dni,
            'num_contacto': persona.num_contacto
        } if persona else None
    }

    return jsonify({
        'access_token': token,
        'response_code': 200,
        'message': 'Login Exitoso',
        'usuario': usuario_data
    }), 200
