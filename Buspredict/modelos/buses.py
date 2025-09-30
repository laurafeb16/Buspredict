from .tipo_buses import TiposBuses
import random

class Bus:
    def __init__(self, numero, ruta, tipo_bus="Metrobus"):
        self.numero = numero
        self.ruta = ruta
        
        # Validar tipo de bus
        if not TiposBuses.validar_tipo(tipo_bus):
            raise ValueError(f"Tipo de bus inválido: {tipo_bus}")
        
        self.tipo_bus = tipo_bus
        self.capacidad = TiposBuses.CAPACIDADES[tipo_bus]
        self.confiabilidad = TiposBuses.CONFIABILIDAD[tipo_bus]
        self.velocidad_promedio = TiposBuses.VELOCIDAD_PROMEDIO[tipo_bus]
        self.retraso_base = TiposBuses.RETRASO_BASE[tipo_bus]
        
        self.pasajeros_actuales = 0
        self.pasajeros = []
        self.posicion_actual = 0
        self.tiempo_llegada_estimado = None
    
    def calcular_retraso_por_tipo(self):
        """Calcula retraso adicional basado en el tipo de bus"""
        # Factor aleatorio basado en confiabilidad
        if random.random() > self.confiabilidad:
            return self.retraso_base + random.randint(0, 10)
        return random.randint(0, self.retraso_base // 2)
    
    def obtener_capacidad_disponible(self):
        """Retorna espacios disponibles en el bus"""
        return max(0, self.capacidad - self.pasajeros_actuales)
    
    def subir_pasajero(self, pasajero):
        """Sube un pasajero respetando la capacidad"""
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            self.pasajeros_actuales = len(self.pasajeros)
            return True
        return False
    
    def bajar_pasajeros(self, cantidad):
        """Baja pasajeros del bus"""
        pasajeros_que_bajan = min(cantidad, self.pasajeros_actuales)
        self.pasajeros_actuales -= pasajeros_que_bajan
        return pasajeros_que_bajan
    
    def __str__(self):
        return f"{self.tipo_bus} #{self.numero} - Ruta {self.ruta} ({self.pasajeros_actuales}/{self.capacidad})"