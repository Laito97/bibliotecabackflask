from flask import jsonify
from app.database import db
from app.models.model_persona import Persona
from app.models.model_usuario import Usuario
from app.models.model_usuario_tipo import UsuarioTipo
from werkzeug.security import generate_password_hash

class UsuarioService:

    @staticmethod
    def listar_usuarios():
        try:
            usuarios = Usuario.query.all()
            usuarios_data = []

            for usuario in usuarios:
                persona = usuario.persona
                usuario_tipo = usuario.usuario_tipo

                usuarios_data.append({
                    'usuario_id': usuario.usuario_id,
                    'usuario_nombre': usuario.usu_nom,
                    'usuario_tipo': {
                        'usuario_tipo_id': usuario_tipo.usuario_tipo_id if usuario_tipo else None,
                        'tipo_nom': usuario_tipo.tipo_nom if usuario_tipo else None,
                    },
                    'persona': {
                        'persona_id': persona.persona_id if persona else None,
                        'nombres': persona.nombres if persona else None,
                        'apellidos': persona.apellidos if persona else None,
                        'dni': persona.dni if persona else None,
                        'correo': persona.correo if persona else None,
                        'num_contacto': persona.num_contacto if persona else None,
                        'direccion': persona.direccion if persona else None
                    }
                })

            return jsonify({
                'response_code': 200,
                'message': 'Usuarios listados exitosamente',
                'usuarios': usuarios_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al listar usuarios: {str(e)}'
            }), 500
        
    @staticmethod
    def guardar_usuario(data):
        try:
            persona_data = data.get('persona')
            password = data.get('password')
            usuario_tipo = data.get('usuario_tipo_id')

            if not persona_data or not password or not usuario_tipo:
                return jsonify({
                    'response_code': 400,
                    'message': 'Faltan datos obligatorios: persona, password o tipo de usuario.'
                }), 400

            persona = Persona(
                nombres=persona_data.get('nombres'),
                apellidos=persona_data.get('apellidos'),
                num_contacto=persona_data.get('num_contacto'),
                correo=persona_data.get('correo'),
                dni=persona_data.get('dni'),
                direccion=persona_data.get('direccion')
            )
            db.session.add(persona)
            db.session.flush()

            usu_nom = f"{persona.nombres.strip()[0].lower()}{persona.apellidos.replace(' ', '').lower()}"

            hashed_password = generate_password_hash(password)

            usuario = Usuario(
                usu_nom=usu_nom,
                usu_pass=hashed_password,
                persona_id=persona.persona_id,
                usuario_tipo_id=usuario_tipo.get('id')
            )
            db.session.add(usuario)
            db.session.commit()

            return jsonify({
                'response_code': 201,
                'message': 'Usuario creado exitosamente',
                'usuario': {
                    'usuario_id': usuario.usuario_id,
                    'usuario_nombre': usuario.usu_nom,
                    'persona_id': persona.persona_id
                }
            }), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'response_code': 500,
                'message': f'Error al guardar usuario: {str(e)}'
            }), 500
    
    @staticmethod
    def listar_usuario_by_id(usuario_id):
        try:
            usuario = Usuario.query.get(usuario_id)

            if not usuario:
                return jsonify({
                    'response_code': 404,
                    'message': 'Usuario no encontrado'
                }), 404

            persona = usuario.persona
            usuario_tipo = usuario.usuario_tipo

            usuario_data = {
                'usuario_id': usuario.usuario_id,
                'usuario_nombre': usuario.usu_nom,
                'usuario_tipo': {
                    'usuario_tipo_id': usuario_tipo.usuario_tipo_id if usuario_tipo else None,
                    'tipo_nom': usuario_tipo.tipo_nom if usuario_tipo else None,
                },
                'persona': {
                    'persona_id': persona.persona_id if persona else None,
                    'nombres': persona.nombres if persona else None,
                    'apellidos': persona.apellidos if persona else None,
                    'dni': persona.dni if persona else None,
                    'correo': persona.correo if persona else None,
                    'num_contacto': persona.num_contacto if persona else None,
                    'direccion': persona.direccion if persona else None
                }
            }

            return jsonify({
                'response_code': 200,
                'message': 'Usuario encontrado exitosamente',
                'usuario': usuario_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al obtener usuario: {str(e)}'
            }), 500


    @staticmethod
    def listar_usuario_tipo():
        try:
            usuario_tipo = UsuarioTipo.query.all()
            usuario_tipo_data = []

            for usuariotipo in usuario_tipo:
                usuario_tipo_id = usuariotipo.usuario_tipo_id
                tipo_nom = usuariotipo.tipo_nom

                usuario_tipo_data.append({
                    'usuario_tipo_id': usuario_tipo_id,
                    'tipo_nom': tipo_nom
                })

            return jsonify({
                'response_code': 200,
                'message': 'Usuarios listados exitosamente',
                'usuario_tipo': usuario_tipo_data
            }), 200

        except Exception as e:
            return jsonify({
                'response_code': 500,
                'message': f'Error al listar usuarios: {str(e)}'
            }), 500