from flask import Flask
from app.config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Registrar blueprints
    from app.routes.main import main_bp
    from app.routes.tarot import tarot_bp
    from app.routes.rituales import rituales_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(tarot_bp, url_prefix='/tarot')
    app.register_blueprint(rituales_bp, url_prefix='/rituales')
    
    # Configurar Jinja2 para mejor rendimiento
    app.jinja_env.auto_reload = False
    app.jinja_env.cache_size = 400
    
    return app
