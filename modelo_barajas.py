import random
from generadores import generar_exponencial, generar_normal

def generar_tiempo_arribo() -> float:
    # Tiempo medio entre llegadas = 20 minutos -> tasa lambda = 1/20
    return generar_exponencial(1.0 / 20.0)

def generar_tiempo_servicio() -> float:
    # 1. Recarga de combustible (Ocurre siempre)
    combustible = generar_exponencial(1.0 / 30.0)
    
    # 2. Maniobras de aterrizaje y despegue (Ocurre siempre)
    maniobra = generar_normal(10.0, 5.0)
    
    # 3. Carga y/o descarga de mercancía (Probabilidad 0.5)
    carga = generar_exponencial(1.0 / 30.0) if random.random() < 0.5 else 0.0
    
    # 4. Reparación de roturas antes del despegue (Probabilidad 0.1)
    reparacion = generar_exponencial(1.0 / 15.0) if random.random() < 0.1 else 0.0
    
    tiempo_total = combustible + maniobra + carga + reparacion
    return max(0.0, tiempo_total)