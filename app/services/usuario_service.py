from app.models.model_usuario import Usuario
from flask import jsonify

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
                    'usuario_tipo': usuario_tipo.tipo_nom if usuario_tipo else None,
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
