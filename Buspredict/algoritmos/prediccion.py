"""
Sistema de predicción de buses con tipos específicos panameños
"""
import random
from datetime import datetime, timedelta
from .factores import aplicar_lluvia, aplicar_factor_quincena
from .búsqueda_secuencial_binaria import minutos_espera
from ..modelos.tipo_buses import TiposBuses  # ✅ Usar la clase original

class PredictorBuses:
    """Sistema de predicción que integra todos los factores"""
    
    def __init__(self):
        self.tipos = TiposBuses()  # ✅ Usar clase original, no duplicar
    
    def predecir_llegada(self, bus, horarios, hora_actual, factores_externos=None):
        """
        Predicción principal que combina todos los algoritmos implementados
        """
        if factores_externos is None:
            factores_externos = {}
        
        # 1. Usar búsqueda binaria para encontrar próximo bus
        minutos_base = minutos_espera(horarios, hora_actual)
        
        # 2. Aplicar retraso por tipo de bus
        retraso_tipo = self._calcular_retraso_por_tipo(bus.tipo_bus)
        
        # 3. Aplicar factores panameños existentes
        minutos_con_lluvia, retraso_lluvia = aplicar_lluvia(minutos_base)
        
        # 4. Aplicar otros factores
        factor_trafico = factores_externos.get('trafico', 1.0)
        factor_quincena_multiplicador = 1.1 if factores_externos.get('es_quincena', False) else 1.0
        
        # 5. Cálculo final
        tiempo_total = (minutos_con_lluvia * factor_trafico * factor_quincena_multiplicador) + retraso_tipo
        
        return {
            'minutos_estimados': max(1, int(tiempo_total)),
            'hora_llegada': self._calcular_hora_llegada(hora_actual, tiempo_total),
            'factores_aplicados': {
                'base': minutos_base,
                'tipo_bus': retraso_tipo,
                'lluvia': retraso_lluvia,
                'trafico': factor_trafico,
                'quincena': factor_quincena_multiplicador
            },
            'confiabilidad': self.tipos.CONFIABILIDAD[bus.tipo_bus]
        }
    
    def _calcular_retraso_por_tipo(self, tipo_bus):
        """Calcula retraso específico del tipo de bus"""
        confiabilidad = self.tipos.CONFIABILIDAD[tipo_bus]
        retraso_base = self.tipos.RETRASO_BASE[tipo_bus]
        
        if random.random() > confiabilidad:
            return retraso_base + random.randint(0, 10)
        return random.randint(0, retraso_base // 2)
    
    def _calcular_hora_llegada(self, hora_actual, minutos_adicionales):
        """Calcula hora exacta de llegada"""
        if isinstance(hora_actual, str):
            hora_actual = datetime.strptime(hora_actual, "%H:%M").time()
        
        ahora = datetime.combine(datetime.today(), hora_actual)
        llegada = ahora + timedelta(minutes=minutos_adicionales)
        return llegada.strftime("%H:%M")
