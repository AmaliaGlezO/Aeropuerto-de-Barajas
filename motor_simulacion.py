import heapq
import random

class SimulacionServidoresParalelo:
    def __init__(self, num_pistas: int, gen_arribo, gen_servicio, tiempo_total: float):
        self.num_pistas = num_pistas
        self.gen_arribo = gen_arribo
        self.gen_servicio = gen_servicio
        self.tiempo_total = tiempo_total

    def ejecutar(self):
        reloj = 0.0
        eventos = []  # Cola de prioridad: (tiempo, tipo_evento, pista_id)
        
        pistas_libres = set(range(self.num_pistas))
        cola_espera = 0
        
        tiempos_inactivos = [0.0] * self.num_pistas
        ultimo_tiempo_libre = [0.0] * self.num_pistas
        
        # Primer arribo
        heapq.heappush(eventos, (self.gen_arribo(), 'ARRIBO', None))

        while eventos:
            tiempo, tipo_evento, pista_id = heapq.heappop(eventos)
            reloj = tiempo

            if tipo_evento == 'ARRIBO':
                if reloj <= self.tiempo_total:
                    siguiente_arribo = reloj + self.gen_arribo()
                    if siguiente_arribo <= self.tiempo_total:
                        heapq.heappush(eventos, (siguiente_arribo, 'ARRIBO', None))
                
                if pistas_libres:
                    # Selección aleatoria uniforme entre pistas libres
                    pista_elegida = random.choice(list(pistas_libres))
                    pistas_libres.remove(pista_elegida)
                    
                    # Acumular inactividad de la pista asignada
                    tiempos_inactivos[pista_elegida] += min(reloj, self.tiempo_total) - ultimo_tiempo_libre[pista_elegida]
                    
                    t_servicio = self.gen_servicio()
                    heapq.heappush(eventos, (reloj + t_servicio, 'SALIDA', pista_elegida))
                else:
                    cola_espera += 1

            elif tipo_evento == 'SALIDA':
                if cola_espera > 0:
                    cola_espera -= 1
                    t_servicio = self.gen_servicio()
                    heapq.heappush(eventos, (reloj + t_servicio, 'SALIDA', pista_id))
                else:
                    pistas_libres.add(pista_id)
                    ultimo_tiempo_libre[pista_id] = min(reloj, self.tiempo_total)

        # Acumular tiempo inactivo final hasta T = 10080 minutos
        for pista in pistas_libres:
            tiempos_inactivos[pista] += self.tiempo_total - ultimo_tiempo_libre[pista]

        return tiempos_inactivos