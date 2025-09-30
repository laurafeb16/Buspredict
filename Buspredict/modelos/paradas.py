from collections import deque

class Parada:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola = deque()  # cola de pasajeros

    def agregar_pasajero(self, pasajero):
        self.cola.append(pasajero)

    def atender_pasajero(self):
        if self.cola:
            return self.cola.popleft()
        return None

    def __str__(self):
        return f"Parada {self.nombre} (Pasajeros en cola: {len(self.cola)})"
