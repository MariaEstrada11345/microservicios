# Microservicios Lab - Sistema de Pedidos

## Descripción
Este proyecto implementa un sistema de microservicios que demuestra conceptos de arquitectura distribuida, incluyendo servicios independientes en diferentes lenguajes de programación, health checks y monitorización.

## Arquitectura
El sistema está compuesto por 4 microservicios:

| Servicio   | Lenguaje | Puerto | Descripción                         |
|------------|----------|--------|-------------------------------------|
| usuarios   | Node.js  | 3001   | Gestión de información de usuarios  |
| pedidos    | Python   | 3002   | Procesamiento de pedidos e integración de datos |
| inventario | Go       | 3003   | Gestión de productos y stock        |
| monitor    | Python   | 3004   | Monitorización y health checks      |

## Instalación y Ejecución

### Prerrequisitos
- Docker
- Docker Compose

### Clonar el repositorio
git clone <repository-url>  
cd microservicios-lab

### Ejecutar todos los servicios
docker-compose up --build

### Ejecutar en segundo plano
docker-compose up -d --build

### Verificar el estado
docker-compose ps

### Comandos Útiles
docker-compose down  
docker-compose logs -f  
docker-compose logs -f monitor  
docker-compose down && docker-compose up --build

## Endpoints Disponibles
### Servicio de Usuarios (Node.js)
GET /usuarios - Lista todos los usuarios  
GET /health - Estado del servicio  

### Servicio de Pedidos (Python)
GET /pedidos - Lista pedidos con datos integrados  
GET /health - Estado del servicio y dependencias  

### Servicio de Inventario (Go)
GET /inventario - Lista productos y stock  
GET /health - Estado del servicio  

### Servicio de Monitor (Python)
GET /status - Estado de todos los servicios  
GET /health - Estado del monitor  
GET /test-connection/<servicio> - Probar conexión específica  

## Probar el Sistema
Verificar salud de servicios individuales:  
curl http://localhost:3001/health  
curl http://localhost:3002/health  
curl http://localhost:3003/health  
curl http://localhost:3004/health  

Probar endpoints principales:  
curl http://localhost:3001/usuarios  
curl http://localhost:3003/inventario  
curl http://localhost:3002/pedidos  

Monitorización:  
curl http://localhost:3004/status  
curl http://localhost:3004/test-connection/usuarios  

## Características Implementadas
Servicio de Inventario en Go:  
- Implementado en lenguaje diferente (Go)  
- Endpoint /inventario funcional  
- Health check integrado  

Integración de Datos Compleja:  
- Servicio de Pedidos combina datos de Usuarios + Inventario  
- Respuestas enriquecidas con información de múltiples fuentes  
- Lógica de negocio para estado de pedidos basado en stock  

Health Checks y Monitorización:  
- Endpoint /health en todos los servicios  
- Servicio de monitor independiente  
- Verificación periódica del estado del sistema  
- Métricas de respuesta y disponibilidad  

## Flujo de Datos
Cliente → Pedidos → Usuarios + Inventario → Respuesta Enriquecida  
  ↓  
Monitor ← Health Checks de todos los servicios  

## Solución de Problemas
Los servicios no se comunican:  
docker network ls  
docker network inspect microservicios-lab_app-network  
docker exec -it <contenedor> ping usuarios  

Error de puertos:  
- Verificar que los puertos 3001-3004 no estén en uso  
- Revisar mapeo de puertos en docker-compose.yml  

Logs de diagnóstico:  
docker-compose logs  
docker-compose logs --tail=50 usuarios  

## Desarrollo
Agregar un nuevo servicio:  
- Crear carpeta con el servicio  
- Agregar Dockerfile  
- Incluir en docker-compose.yml  
- Actualizar el monitor si es necesario  

Modificar un servicio existente:  
docker-compose build <nombre-servicio>  
docker-compose up -d <nombre-servicio>  

## Licencia
Este es un proyecto educativo para demostrar conceptos de microservicios.
