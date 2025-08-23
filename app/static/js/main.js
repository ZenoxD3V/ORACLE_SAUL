// Optimización de carga del mapa
class MapLoader {
    constructor() {
        this.mapContainer = document.getElementById('mapa-placeholder');
        this.mapLoaded = false;
        this.init();
    }

    init() {
        // Cargar mapa cuando el usuario esté cerca de la sección
        this.setupIntersectionObserver();
        
        // Precargar mapa después de 3 segundos de que la página cargue
        setTimeout(() => {
            if (!this.mapLoaded) {
                this.preloadMap();
            }
        }, 3000);
    }

    setupIntersectionObserver() {
        const ubicacionSection = document.getElementById('ubicacion');
        
        if ('IntersectionObserver' in window && ubicacionSection) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    // Cargar cuando la sección esté a 200px de ser visible
                    if (entry.isIntersecting && !this.mapLoaded) {
                        this.loadMap();
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                rootMargin: '200px 0px' // Cargar 200px antes
            });

            observer.observe(ubicacionSection);
        } else {
            // Fallback para navegadores sin soporte
            this.preloadMap();
        }
    }

    preloadMap() {
        // Precargar de forma invisible
        const preloadFrame = document.createElement('iframe');
        preloadFrame.style.display = 'none';
        preloadFrame.src = 'https://maps.google.com/maps?q=Puerto%20Grau%20Tarapacá%2C%20Amazonas&t=m&z=10&output=embed&iwloc=near';
        document.body.appendChild(preloadFrame);
        
        setTimeout(() => {
            document.body.removeChild(preloadFrame);
        }, 5000);
    }

    loadMap() {
        if (this.mapLoaded || !this.mapContainer) return;

        const iframe = document.createElement('iframe');
        iframe.src = 'https://maps.google.com/maps?q=Puerto%20Grau%20Tarapacá%2C%20Amazonas&t=m&z=10&output=embed&iwloc=near';
        iframe.width = '100%';
        iframe.height = '450';
        iframe.style.border = 'none';
        iframe.style.borderRadius = '15px';
        iframe.allowFullscreen = true;
        iframe.loading = 'lazy';
        iframe.referrerPolicy = 'no-referrer-when-downgrade';

        // Reemplazar placeholder con mapa real
        this.mapContainer.innerHTML = '';
        this.mapContainer.appendChild(iframe);
        this.mapContainer.className = 'mapa-container';
        
        this.mapLoaded = true;
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    new MapLoader();
});
