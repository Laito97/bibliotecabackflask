from app.database import db

class Libro(db.Model):
    __tablename__ = 'libros'

    libro_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(15))
    url_portada = db.Column(db.String(250))
    libro_nom = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    anio_publicacion = db.Column(db.String(4))
    edicion = db.Column(db.String(100))
    existencias = db.Column(db.Integer)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.categoria_id'))
    editorial_id = db.Column(db.Integer, db.ForeignKey('editoriales.editorial_id'))
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.autor_id'))
    fecha_creacion = db.Column(db.DateTime)
    usuario_creacion_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    fecha_actualizacion = db.Column(db.DateTime)
    usuario_actualizacion_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.estado_id'))

    # Relaciones
    categoria = db.relationship('Categoria', backref='libros')
    editorial = db.relationship('Editorial', backref='libros')
    autor = db.relationship('Autor', backref='libros')
    usuario_creacion = db.relationship('Usuario', foreign_keys=[usuario_creacion_id])
    usuario_actualizacion = db.relationship('Usuario', foreign_keys=[usuario_actualizacion_id])
    estado = db.relationship('Estado', foreign_keys=[estado_id])