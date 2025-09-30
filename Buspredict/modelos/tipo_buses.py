class TiposBuses:
    """Definición de los tipos de buses en Panamá"""
    
    # Capacidades por tipo de bus
    CAPACIDADES = {
        "DiabloRojo": 45,
        "Metrobus": 80, 
        "Chiva": 25
    }
    
    # Factor de confiabilidad según tipo (puntualidad)
    CONFIABILIDAD = {
        "DiabloRojo": 0.65,  # 65% de puntualidad
        "Metrobus": 0.85,    # 85% de puntualidad  
        "Chiva": 0.55        # 55% de puntualidad
    }
    
    # Factor de velocidad promedio (km/h en ciudad)
    VELOCIDAD_PROMEDIO = {
        "DiabloRojo": 25,    # Más lento por paradas frecuentes
        "Metrobus": 35,      # Más rápido por carriles exclusivos
        "Chiva": 20          # Más lento por condiciones rurales
    }
    
    # Factor de retraso adicional por tipo
    RETRASO_BASE = {
        "DiabloRojo": 8,     # 8 minutos promedio de retraso
        "Metrobus": 3,       # 3 minutos promedio de retraso
        "Chiva": 12          # 12 minutos promedio de retraso
    }
    
    @classmethod
    def obtener_tipos_disponibles(cls):
        """Retorna lista de tipos de buses disponibles"""
        return list(cls.CAPACIDADES.keys())
    
    @classmethod
    def validar_tipo(cls, tipo_bus):
        """Valida si el tipo de bus existe"""
        return tipo_bus in cls.CAPACIDADES
