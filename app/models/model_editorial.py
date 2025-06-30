from app.database import db

class Editorial(db.Model):
    __tablename__ = 'editoriales'

    editorial_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    editorial_nom = db.Column(db.String(250))
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.estado_id'))
    fecha_actualizacion = db.Column(db.DateTime)
    usuario_actualizacion_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))

    estado = db.relationship('Estado', foreign_keys=[estado_id])
    usuario_actualizacion = db.relationship('Usuario', foreign_keys=[usuario_actualizacion_id])
<<<<<<< HEAD
=======

>>>>>>> 9525f9dd2aaa0e57a4e2a6e28fc3e263e20ee57c
