import time
import redis
from flask import Flask

app = Flask(__name__)
# Conexión al contenedor Redis
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    # Intento de lectura en Caché Nivel 2 (Redis)
    val = cache.get('hit_count')
    if val:
        return f"Respuesta desde Redis (Nivel 2): Hola! Este dato ya estaba cacheado."

    # Simulación de proceso lento (3 segundos)
    time.sleep(3)
    cache.setex('hit_count', 30, "true") # Guardar 30 seg
    return "Proceso lento finalizado. Dato guardado en Redis."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
