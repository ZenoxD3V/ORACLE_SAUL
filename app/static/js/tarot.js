class TarotConsulta {
    constructor() {
        this.initEventListeners();
    }
    
    initEventListeners() {
        document.getElementById('consulta-form')?.addEventListener('submit', (e) => {
            e.preventDefault();
            this.realizarConsulta();
        });
    }
    
    async realizarConsulta() {
        const pregunta = document.getElementById('pregunta').value;
        const tipo = document.getElementById('tipo-lectura').value;
        
        try {
            const response = await fetch('/tarot/lectura', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ pregunta, tipo })
            });
            
            const resultado = await response.json();
            this.mostrarResultado(resultado);
        } catch (error) {
            console.error('Error en consulta:', error);
        }
    }
    
    mostrarResultado(resultado) {
        const container = document.getElementById('resultado-lectura');
        container.innerHTML = this.renderizarCartas(resultado.cartas);
        container.style.display = 'block';
    }
    
    renderizarCartas(cartas) {
        return `
            <div class="lectura-resultado">
                <div class="carta-container">
                    <div class="tarot-card">
                        <h3>Pasado</h3>
                        <p>${cartas.pasado.nombre}</p>
                        <p>${cartas.pasado.significado}</p>
                    </div>
                    <div class="tarot-card">
                        <h3>Presente</h3>
                        <p>${cartas.presente.nombre}</p>
                        <p>${cartas.presente.significado}</p>
                    </div>
                    <div class="tarot-card">
                        <h3>Futuro</h3>
                        <p>${cartas.futuro.nombre}</p>
                        <p>${cartas.futuro.significado}</p>
                    </div>
                </div>
            </div>
        `;
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    new TarotConsulta();
});
