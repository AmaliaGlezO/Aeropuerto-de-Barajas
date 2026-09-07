# Simulación de Eventos Discretos - Aeropuerto de Barajas

Este proyecto implementa un Modelo de Simulación de Eventos Discretos (SED) para estimar el tiempo total de inactividad de las 5 pistas de aterrizaje de aviones de carga en el Aeropuerto de Barajas durante un horizonte temporal de 1 semana (10 080 minutos).

## Estructura del Proyecto

El código está desacoplado en 4 módulos principales:

* **`generadores.py`**: Implementación manual de generadores de variables aleatorias estocásticas (distribución exponencial mediante transformada inversa y distribución normal mediante Box-Müller).
* **`modelo_barajas.py`**: Modelación del dominio del aeropuerto. Define la frecuencia de arribos y la suma estocástica de los tiempos de estancia en pista (combustible, maniobras, carga/descarga y reparaciones).
* **`motor_simulacion.py`**: Motor de eventos discretos para $k$ servidores en paralelo con cola de prioridad (`heapq`), asignación aleatoria uniforme de pistas libres y registro acotado del tiempo inactivo.
* **`MAIN.py`**: Script principal de experimentación. Corre réplicas independientes hasta alcanzar un error estándar inferior a $d = 10$ minutos en todas las pistas.

