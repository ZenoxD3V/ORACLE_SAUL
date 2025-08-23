from flask import Blueprint, render_template, jsonify
from datetime import datetime
from app.utils.lunar_calendar import get_lunar_phase

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    current_phase = get_lunar_phase()
    return render_template('index.html', 
                         lunar_phase=current_phase,
                         current_date=datetime.now(),
                         current_year=datetime.now().year,
                         page_title="Templo del Maestro Saúl de la Cruz")

@main_bp.route('/api/lunar-phase')
def lunar_phase_api():
    phase = get_lunar_phase()
    return jsonify({
        'phase': phase['name'],
        'percentage': phase['percentage'],
        'energy': phase['energy_type']
    })


@main_bp.route('/tarot')
def tarot_gratis():
    """Página dedicada al tarot gratuito"""
    return render_template('tarot/gratis.html',
                         page_title="Tarot Gratis - Maestro Saúl")

@main_bp.route('/testimonios')
def testimonios():
    """Página de testimonios"""
    testimonios_data = [
        {
            'nombre': 'Carmen Cubillos',
            'ubicacion': 'Bogotá, Colombia',
            'fecha': '18 de mayo de 2025',
            'testimonio': 'Me sentía perdida y sin energía, pero con la limpieza espiritual...'
        },
        # ... más testimonios
    ]
    return render_template('testimonios.html', 
                         testimonios=testimonios_data)
