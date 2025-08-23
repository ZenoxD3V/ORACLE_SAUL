from flask import Blueprint, render_template, request, jsonify
from app.utils.tarot_engine import TarotReading
import random

tarot_bp = Blueprint('tarot', __name__)

@tarot_bp.route('/')
def index():
    return render_template('tarot/consulta.html')

@tarot_bp.route('/lectura', methods=['POST'])
def lectura():
    pregunta = request.json.get('pregunta', '')
    tipo_lectura = request.json.get('tipo', 'tres_cartas')
    
    reading = TarotReading()
    resultado = reading.realizar_lectura(pregunta, tipo_lectura)
    
    return jsonify(resultado)

@tarot_bp.route('/carta-del-dia')
def carta_del_dia():
    reading = TarotReading()
    carta = reading.carta_diaria()
    return render_template('tarot/carta_del_dia.html', carta=carta)
