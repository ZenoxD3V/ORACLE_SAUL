import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ORACLESAUL'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    
    # Configuraciones de rendimiento
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 año cache para static files
    TEMPLATES_AUTO_RELOAD = False
    
    # Configuraciones esotéricas
    LUNAR_API_KEY = os.environ.get('LUNAR_API_KEY', '')
    TAROT_DECK_SIZE = 78
