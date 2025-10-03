# -*- coding: utf-8 -*-
def ordenar_por_tiempo_total(buses_info):
    """
    Ordena buses por tiempo total (espera + viaje) - menor a mayor
    buses_info: lista de diccionarios con 'bus', 'tiempo_espera', 'tiempo_viaje'
    """
    return sorted(buses_info, key=lambda x: x['tiempo_espera'] + x['tiempo_viaje'])

def clasificar_buses_por_eficiencia(buses):
    """
    Clasifica buses por eficiencia (velocidad/retraso)
    """
    return sorted(buses, key=lambda bus: bus.velocidad_promedio / bus.retraso_base, reverse=True)

def ordenar_buses_por_tiempo(buses_data):
    """
    Ordena buses por tiempo total ascendente
    """
    return sorted(buses_data, key=lambda x: x['tiempo_total'])

def optimizar_horarios_por_dia():
    """
    Retorna horarios optimizados para diferentes momentos del día
    """
    return {
        'mañana_temprano': '06:30',
        'entre_rush': '10:15', 
        'noche': '21:00'
    }

def clasificacion_quicksort(datos, campo_clave):
    """
    Implementación de QuickSort para ordenar por un campo específico
    """
    if len(datos) <= 1:
        return datos
    
    pivot = datos[len(datos) // 2]
    pivot_valor = pivot[campo_clave]
    
    menores = [x for x in datos if x[campo_clave] < pivot_valor]
    iguales = [x for x in datos if x[campo_clave] == pivot_valor]
    mayores = [x for x in datos if x[campo_clave] > pivot_valor]
    
    return clasificacion_quicksort(menores, campo_clave) + iguales + clasificacion_quicksort(mayores, campo_clave)