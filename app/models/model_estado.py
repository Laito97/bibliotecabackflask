from app.database import db

class Estado(db.Model):
    __tablename__ = 'estado'

    estado_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(20))

    usuario = db.relationship('Usuario', back_populates='estado')
