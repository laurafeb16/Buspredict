import bisect
from datetime import datetime, time

# --- Utilidades de tiempo ---
def convertir_hora(hora_str: str) -> time:
    """'HH:MM' -> datetime.time"""
    return datetime.strptime(hora_str, "%H:%M").time()

def ordenar_horarios(horarios):
    """Acepta list[str|time] y devuelve list[time] ordenada ascendente."""
    arr = [convertir_hora(h) if isinstance(h, str) else h for h in horarios]
    return sorted(arr)

def _to_minutes(t: time) -> int:
    return t.hour * 60 + t.minute

# --- Búsquedas ---
def busqueda_secuencial(horarios, hora_actual):
    """
    Devuelve (idx, hora_time) del próximo bus >= hora_actual.
    Si no hay más buses en el día, retorna (None, None).
    """
    hlist = ordenar_horarios(horarios)
    hora_actual = convertir_hora(hora_actual) if isinstance(hora_actual, str) else hora_actual
    for i, h in enumerate(hlist):
        if h >= hora_actual:
            return i, h
    return None, None

def busqueda_binaria(horarios, hora_actual):
    """
    Igual que la secuencial, pero usando bisect (búsqueda binaria).
    """
    hlist = ordenar_horarios(horarios)
    hora_actual = convertir_hora(hora_actual) if isinstance(hora_actual, str) else hora_actual
    idx = bisect.bisect_left(hlist, hora_actual)
    if idx < len(hlist):
        return idx, hlist[idx]
    return None, None

def proximo_bus_ciclico(horarios, hora_actual):
    """
    Devuelve el próximo bus, envolviendo a la primera hora del día siguiente si hace falta.
    Retorna (idx, hora_time, wrap), donde wrap = 0 (mismo día) o 1 (día siguiente).
    """
    hlist = ordenar_horarios(horarios)
    hora_actual = convertir_hora(hora_actual) if isinstance(hora_actual, str) else hora_actual
    idx = bisect.bisect_left(hlist, hora_actual)
    if idx < len(hlist):
        return idx, hlist[idx], 0
    return 0, hlist[0], 1

def minutos_espera(horarios, hora_actual) -> int:
    """
    Minutos hasta el próximo bus. Si envuelve al día siguiente, suma 24h.
    """
    idx, hprox, wrap = proximo_bus_ciclico(horarios, hora_actual)
    hora_actual = convertir_hora(hora_actual) if isinstance(hora_actual, str) else hora_actual
    cur = _to_minutes(hora_actual)
    nxt = _to_minutes(hprox) + (1440 if wrap else 0)
    return nxt - cur