class Bus:
    def __init__(self, bus_id, ruta, capacidad, horario):
        self.bus_id = bus_id
        self.ruta = ruta
        self.capacidad = capacidad
        self.horario = horario  # lista de horas de paso
        self.pasajeros = []

    def subir_pasajero(self, pasajero):
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            return True
        return False

    def __str__(self):
        return f"Bus {self.bus_id} - Ruta {self.ruta} (Capacidad {self.capacidad})"
