from app.database import db

class Autor(db.Model):
    __tablename__ = 'autores'

    autor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    autor_nom = db.Column(db.String(250))
    fecha_creacion = db.Column(db.DateTime)
    usuario_creacion_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    fecha_actualizacion = db.Column(db.DateTime)
    usuario_actualizacion_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))

    # Relaciones
    usuario_creacion = db.relationship('Usuario', foreign_keys=[usuario_creacion_id])
    usuario_actualizacion = db.relationship('Usuario', foreign_keys=[usuario_actualizacion_id])
