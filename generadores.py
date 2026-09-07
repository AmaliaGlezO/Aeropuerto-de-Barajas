import math
import random

def generar_exponencial(tasa: float) -> float:
    u = random.random()
    return -math.log(1.0 - u) / tasa

def generar_normal(media: float, desviacion: float) -> float:
    u1 = random.random()
    u2 = random.random()
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    return media + z0 * desviacion