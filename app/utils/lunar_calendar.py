import math
from datetime import datetime

def get_lunar_phase():
    now = datetime.now()
    
    # Cálculo simplificado de fase lunar
    days_since_new = (now - datetime(2000, 1, 6)).days % 29.53
    phase_percentage = (days_since_new / 29.53) * 100
    
    if phase_percentage < 6.25:
        phase = "Luna Nueva"
        energy = "renovacion"
    elif phase_percentage < 43.75:
        phase = "Luna Creciente"
        energy = "crecimiento"
    elif phase_percentage < 56.25:
        phase = "Luna Llena"
        energy = "culminacion"
    else:
        phase = "Luna Menguante"
        energy = "liberacion"
    
    return {
        'name': phase,
        'percentage': round(phase_percentage, 1),
        'energy_type': energy
    }
