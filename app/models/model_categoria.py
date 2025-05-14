from app.database import db

class Categoria(db.Model):
    __tablename__ = 'cateogrias'

    categoria_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoria_nom = db.Column(db.String(250))
