from app.database import db

class Persona(db.Model):
    __tablename__ = 'persona'

    persona_id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    num_contacto = db.Column(db.String(9))
    correo = db.Column(db.String(50))
    dni = db.Column(db.Integer, unique=True)
    direccion = db.Column(db.String(100))

    # Relaciones inversas
    usuario = db.relationship('Usuario', back_populates='persona', uselist=False)

