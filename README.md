# Práctica 10 - Proxy Inverso y Caché (SAD)

## 1. Descripción
Este proyecto consiste en el despliegue de una infraestructura de microservicios diseñada bajo tres pilares: **Seguridad Perimetral**, **Alto Rendimiento** y **Buenas Prácticas DevOps**. El sistema utiliza contenedores aislados en una red privada donde solo el puerto 80 es accesible desde el exterior.

## 2. Diagrama de la Arquitectura
![Diagrama de Arquitectura](https://raw.githubusercontent.com/fherper1606/practica10-proxy/main/Diagrama.png)


## 3. Instrucciones de Despliegue
Para clonar y levantar el entorno completo, ejecuta los siguientes comandos en tu terminal de Ubuntu:

```bash
# Clonar el repositorio
git clone https://github.com/fherper1606/practica10-proxy.git
cd practica10-proxy

# Levantar el entorno con Docker Compose
sudo docker compose up -d --build
```

## 4. Pruebas de Verificación
Para comprobar que el sistema de caché funciona correctamente, utiliza los comandos `curl` para observar los tiempos de respuesta y las cabeceras HTTP:

### Verificación de Caché Nivel 1 (Nginx)
Ejecuta el siguiente comando dos veces:
```bash
curl -I http://localhost
```
* **Primera vez:** Verás `X-Proxy-Cache: MISS` y un retraso de 3 segundos (la API está procesando).
* **Segunda vez:** Verás `X-Proxy-Cache: HIT` y respuesta instantánea (servido desde la caché de Nginx).

### Verificación de Seguridad
Comprueba que los servicios internos no son accesibles directamente desde el host:
* `curl http://localhost:5000` -> Debe fallar.
* `curl http://localhost:6379` -> Debe fallar.

