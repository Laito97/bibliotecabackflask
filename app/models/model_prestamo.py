from app.database import db

class Prestamo(db.Model):
    __tablename__ = 'prestamos'

    prestamo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libro_id = db.Column(db.Integer, db.ForeignKey('libros.libro_id'))
    usuario_solicita_prestamo = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    usuario_aprueba_prestamo = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    fecha_solicitud_prestamo = db.Column(db.DateTime)
    fecha_devolucion_prestamo = db.Column(db.DateTime)
    prestamo_estado_id = db.Column(db.Integer, db.ForeignKey('prestamos_estado.prestamo_estado_id'))
    fecha_creacion = db.Column(db.DateTime)
    usuario_creacion_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    fecha_actualizacion = db.Column(db.DateTime)
    usuario_actualizacion_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))

    # Relaciones
    libro = db.relationship('Libro', backref='prestamos')
    usuario_solicita = db.relationship('Usuario', foreign_keys=[usuario_solicita_prestamo])
    usuario_aprueba = db.relationship('Usuario', foreign_keys=[usuario_aprueba_prestamo])
    prestamo_estado = db.relationship('PrestamoEstado', back_populates='prestamos')
    usuario_creacion = db.relationship('Usuario', foreign_keys=[usuario_creacion_id])
    usuario_actualizacion = db.relationship('Usuario', foreign_keys=[usuario_actualizacion_id])
