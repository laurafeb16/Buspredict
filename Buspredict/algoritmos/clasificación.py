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
