from statistics import mean, pstdev

class TablaHash:
    """
    En Python, dict ya es un hash table, pero lo envolvemos
    para practicar API típica de tablas hash.
    """
    def __init__(self):
        self._data = {}

    def set(self, clave, valor):
        self._data[clave] = valor

    def get(self, clave, default=None):
        return self._data.get(clave, default)

    def contiene(self, clave) -> bool:
        return clave in self._data

    def eliminar(self, clave):
        self._data.pop(clave, None)

    def claves(self):
        return list(self._data.keys())

    def items(self):
        return self._data.items()

class RegistroEspera:
    """
    Guarda tiempos de espera (en minutos) por ruta
    y genera estadísticas descriptivas simples.
    """
    def __init__(self):
        self._tiempos_por_ruta = {}  # ruta -> list[int]

    def agregar(self, ruta: str, minutos: int):
        self._tiempos_por_ruta.setdefault(ruta, []).append(minutos)

    def resumen(self, ruta: str):
        arr = self._tiempos_por_ruta.get(ruta, [])
        if not arr:
            return {"n": 0, "promedio": None, "min": None, "max": None, "desv": None}
        return {
            "n": len(arr),
            "promedio": round(mean(arr), 2),
            "min": min(arr),
            "max": max(arr),
            "desv": round(pstdev(arr), 2) if len(arr) > 1 else 0.0
        }

    def todas(self):
        return {ruta: self.resumen(ruta) for ruta in self._tiempos_por_ruta}
