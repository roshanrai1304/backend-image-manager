from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    # Apply CORS to all routes
    CORS(app, supports_credentials=True)
    
    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.images import images_bp
    from .routes.health import health_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(images_bp, url_prefix='/api/images')
    app.register_blueprint(health_bp, url_prefix='/')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app 