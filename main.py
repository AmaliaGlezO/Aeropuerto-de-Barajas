import math
import numpy as np
from modelo_barajas import generar_tiempo_arribo, generar_tiempo_servicio
from motor_simulacion import SimulacionServidoresParalelo

def correr_experimento(error_tolerado=10.0, tamano_bloque=10):
    T = 10080.0  # 1 semana en minutos (7 * 24 * 60)
    num_pistas = 5
    resultados = [[] for _ in range(num_pistas)]
    
    n = 0
    while True:
        for _ in range(tamano_bloque):
            sim = SimulacionServidoresParalelo(num_pistas, generar_tiempo_arribo, generar_tiempo_servicio, T)
            inactividad = sim.ejecutar()
            for i in range(num_pistas):
                resultados[i].append(inactividad[i])
        
        n += tamano_bloque
        medias = [float(np.mean(resultados[i])) for i in range(num_pistas)]
        desviaciones = [float(np.std(resultados[i], ddof=1)) for i in range(num_pistas)]
        errores_est = [s / math.sqrt(n) for s in desviaciones]
        
        if max(errores_est) < error_tolerado:
            break

    print(f"Simulación finalizada tras {n} réplicas independientes.")
    print("-" * 55)
    print(f"{'Pista':<8}{'Inactividad Media (min)':<25}{'Error Est. (min)':<20}")
    print("-" * 55)
    for i in range(num_pistas):
        print(f"{i+1:<8}{medias[i]:<25.1f}{errores_est[i]:<20.2f}")
    print("-" * 55)
    promedio_global = np.mean(medias)
    print(f"Promedio global de inactividad: {promedio_global:.1f} min ({promedio_global/T*100:.1f}% del tiempo semanal)")

if __name__ == "__main__":
    correr_experimento()