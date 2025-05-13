from app.database import db

class Editorial(db.Model):
    __tablename__ = 'editoriales'

    editorial_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    editorial_nom = db.Column(db.String(250))
