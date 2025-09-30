class Pasajero:
    def __init__(self, pasajero_id, destino, hora_llegada):
        self.pasajero_id = pasajero_id
        self.destino = destino
        self.hora_llegada = hora_llegada

    def __str__(self):
        return f"Pasajero {self.pasajero_id} → {self.destino} (llegó {self.hora_llegada})"
