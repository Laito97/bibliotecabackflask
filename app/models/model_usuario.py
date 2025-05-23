from app.database import db
from app.models.model_persona import Persona
from app.models.model_usuario_tipo import UsuarioTipo  # Asegúrate de tener este modelo

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True)
    usu_nom = db.Column(db.String(50))
    usu_pass = db.Column(db.String(50))

    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id'))
    usuario_tipo_id = db.Column(db.Integer, db.ForeignKey('usuarios_tipo.usuario_tipo_id'))

    # Relaciones
    persona = db.relationship('Persona', back_populates='usuario', uselist=False)
    usuario_tipo = db.relationship('UsuarioTipo', back_populates='usuarios', uselist=False)

