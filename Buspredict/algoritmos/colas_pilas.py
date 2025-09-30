from collections import deque

# --- Cola (Queue) ---
class Cola:
    def __init__(self):
        self._q = deque()

    def encolar(self, x):
        self._q.append(x)

    def desencolar(self):
        return self._q.popleft() if self._q else None

    def frente(self):
        return self._q[0] if self._q else None

    def vacia(self) -> bool:
        return len(self._q) == 0

    def tamanio(self) -> int:
        return len(self._q)

# --- Pila (Stack) ---
class Pila:
    def __init__(self):
        self._s = []

    def apilar(self, x):
        self._s.append(x)

    def desapilar(self):
        return self._s.pop() if self._s else None

    def cima(self):
        return self._s[-1] if self._s else None

    def vacia(self) -> bool:
        return len(self._s) == 0

    def tamanio(self) -> int:
        return len(self._s)

# --- Utilidad: abordar desde una Parada del módulo modelos ---
def abordar_desde_parada(parada, bus, max_subidas=None) -> int:
    """
    Toma pasajeros desde parada.cola (usando parada.atender_pasajero)
    y los sube al bus respetando su capacidad.
    Retorna la cantidad que subió.
    (Duck typing: no importamos modelos para evitar ciclos)
    """
    subidos = 0
    cap_disp = bus.capacidad - len(bus.pasajeros)
    limite = cap_disp if max_subidas is None else min(cap_disp, max_subidas)

    # parada debe tener: .cola (colección) y .atender_pasajero()
    while len(parada.cola) > 0 and subidos < limite:
        p = parada.atender_pasajero()
        if bus.subir_pasajero(p):
            subidos += 1
        else:
            break
    return subidos
