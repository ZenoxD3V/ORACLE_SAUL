import random
from datetime import datetime

class TarotReading:
    def __init__(self):
        self.arcanos_mayores = [
            {"nombre": "El Loco", "numero": 0, "significado": "Nuevos comienzos, espontaneidad"},
            {"nombre": "El Mago", "numero": 1, "significado": "Poder personal, habilidades"},
            {"nombre": "La Sacerdotisa", "numero": 2, "significado": "Intuición, misterio"},
            # ... agregar las 78 cartas completas
        ]
    
    def realizar_lectura(self, pregunta, tipo='tres_cartas'):
        cartas_seleccionadas = random.sample(self.arcanos_mayores, 3)
        
        if tipo == 'tres_cartas':
            return {
                'pregunta': pregunta,
                'cartas': {
                    'pasado': cartas_seleccionadas[0],
                    'presente': cartas_seleccionadas[1],
                    'futuro': cartas_seleccionadas[2]
                },
                'interpretacion': self._generar_interpretacion(cartas_seleccionadas, pregunta)
            }
    
    def carta_diaria(self):
        # Usar fecha como semilla para consistencia diaria
        random.seed(datetime.now().strftime('%Y%m%d'))
        return random.choice(self.arcanos_mayores)
    
    def _generar_interpretacion(self, cartas, pregunta):
        # Lógica para generar interpretación basada en las cartas y pregunta
        return "Interpretación personalizada basada en tu consulta..."
