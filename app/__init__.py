from flask import Flask
from .config import Config
from .database import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.routes.auth_routes import auth_bp
from app.routes.usuario_routes import usuario_bp
from app.routes.autor_routes import autor_bp
from app.routes.editorial_routes import editorial_bp
from app.routes.categoria_routes import categoria_bp
from app.routes.libro_routes import libro_bp
from app.routes.prestamo_routes import prestamo_bp


jwt = JWTManager()
prefix = '/api/biblioteca_v1'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    CORS(app)

    app.register_blueprint(auth_bp, url_prefix=prefix)
    app.register_blueprint(usuario_bp, url_prefix=prefix)
    app.register_blueprint(autor_bp, url_prefix=prefix)
    app.register_blueprint(editorial_bp, url_prefix=prefix)
    app.register_blueprint(categoria_bp, url_prefix=prefix)
    app.register_blueprint(libro_bp, url_prefix=prefix)
    app.register_blueprint(prestamo_bp, url_prefix=prefix)

    return app
