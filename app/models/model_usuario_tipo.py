from app.database import db

class UsuarioTipo(db.Model):
    __tablename__ = 'usuarios_tipo'

    usuario_tipo_id = db.Column(db.Integer, primary_key=True)
    tipo_nom = db.Column(db.String(100))

    # Relación inversa
    usuarios = db.relationship('Usuario', back_populates='usuario_tipo')

