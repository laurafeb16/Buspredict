import random
from datetime import datetime

def es_quincena(fecha=None):
    """
    Devuelve True si la fecha es 15 o 30 del mes.
    """
    if fecha is None:
        fecha = datetime.now().date()
    return fecha.day in (15, 30)

def aplicar_factor_quincena(num_pasajeros):
    """
    Si es quincena, aumenta la cantidad de pasajeros (ej. +30%).
    """
    if es_quincena():
        aumento = int(num_pasajeros * 0.3) + 1
        return num_pasajeros + aumento
    return num_pasajeros

def aplicar_lluvia(minutos_espera, probabilidad=0.3):
    """
    Con cierta probabilidad (30% por defecto), añade un retraso aleatorio de 5–15 minutos.
    """
    if random.random() < probabilidad:
        retraso = random.randint(5, 15)
        return minutos_espera + retraso, retraso
    return minutos_espera, 0
