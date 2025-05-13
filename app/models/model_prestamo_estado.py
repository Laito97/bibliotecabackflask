from app.database import db

class PrestamoEstado(db.Model):
    __tablename__ = 'prestamos_estado'

    prestamo_estado_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(20))
