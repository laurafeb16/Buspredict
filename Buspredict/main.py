from Buspredict.modelos import Bus, Parada, Pasajero
from Buspredict.algoritmos import (
    convertir_hora,
    busqueda_binaria,
    minutos_espera,
    abordar_desde_parada,
    RegistroEspera,
    es_quincena,
    aplicar_factor_quincena,
    aplicar_lluvia,
)
from Buspredict.algoritmos.clasificación import (
    ordenar_buses_por_tiempo,
    optimizar_horarios_por_dia,
    clasificacion_quicksort
)
from Buspredict.visualización.gráficos import mostrar_graficos_demo
import random
from datetime import datetime


def demo_espectacular():
    """
    DEMO
    Comparación y optimización inteligente
    """
    print("\n" + "="*60)
    print("BUSPREDICT")
    print("="*60)
    
    # === COMPARACIÓN DRAMÁTICA EN VIVO ===
    print("\nCOMPARACIÓN:")
    print("-" * 40)
    
    # Simular día normal vs día 15 con lluvia
    ruta_ejemplo = "5 de Mayo → Albrook"
    tiempo_base = 12
    
    # Día normal
    print(f"Día normal (5 de Mayo): {tiempo_base} minutos")
    
    # Día 15 con lluvia
    tiempo_quincena = aplicar_factor_quincena(tiempo_base)
    tiempo_final, retraso_lluvia = aplicar_lluvia(tiempo_quincena, probabilidad=1.0)
    
    print(f"Día 15 con lluvia tropical: {tiempo_final} minutos")
    print(f"{tiempo_final - tiempo_base} minutos extra solo por ser panameño y entender el país")
    
    # === OPTIMIZACIÓN ===
    print("\nOPTIMIZACIÓN:")
    print("-" * 30)
    
    horarios_opt = optimizar_horarios_por_dia()
    print(" Mejores horarios para hoy:")
    print(f"1. {horarios_opt['mañana_temprano']} hrs - 8 min (antes del caos matutino)")
    print(f"2. {horarios_opt['entre_rush']} hrs - 11 min (entre horas pico)")  
    print(f"3. {horarios_opt['noche']} hrs - 9 min (Diablos Rojos ya no corren)")
    
    # === DATOS SIMULADOS DE BUSES ===
    buses_data = [
        {'tipo': 'Diablos Rojos', 'tiempo_espera': 15, 'tiempo_viaje': 25, 'confiabilidad': 0.65},
        {'tipo': 'Metrobús', 'tiempo_espera': 8, 'tiempo_viaje': 18, 'confiabilidad': 0.85},
        {'tipo': 'Chiva', 'tiempo_espera': 12, 'tiempo_viaje': 22, 'confiabilidad': 0.70}
    ]
    
    # Calcular tiempo total
    for bus in buses_data:
        bus['tiempo_total'] = bus['tiempo_espera'] + bus['tiempo_viaje']
    
    # Ordenar por eficiencia
    buses_ordenados = ordenar_buses_por_tiempo(buses_data)
    
    print("\nRANKING DE EFICIENCIA:")
    print("-" * 25)
    for i, bus in enumerate(buses_ordenados, 1):
        print(f"{i}. {bus['tipo']} - {bus['tiempo_total']} min total "
              f"(Confiabilidad: {int(bus['confiabilidad']*100)}%)")
    
    # === GRÁFICOS IMPACTANTES ===
    print("\n Generando gráficos...")
    try:
        mostrar_graficos_demo()
    except ImportError:
        print(" Para ver gráficos, instala: pip install matplotlib")


def simulacion_completa():
    """Simulación completa del sistema"""
    print("\n SIMULACIÓN COMPLETA DEL SISTEMA")
    print("=" * 40)
    
    # Crear buses y paradas
    horarios = ["07:00", "07:15", "07:30", "08:00", "08:30"]
    bus1 = Bus(1, "Via España", "Metrobus")
    parada1 = Parada("5 de Mayo")
    
    # Agregar pasajeros (aplicando factor quincena si corresponde)
    pasajeros_base = 5
    pasajeros_final = aplicar_factor_quincena(pasajeros_base)
    
    print(f"Pasajeros base: {pasajeros_base}")
    if es_quincena():
        print(f"Factor quincena aplicado → Pasajeros ahora: {pasajeros_final}")
    
    for i in range(pasajeros_final):
        parada1.agregar_pasajero(Pasajero(i+1, f"Destino {i+1}", "07:05"))
    
    # Predicción con factores climáticos
    hora_actual = "07:10"
    espera_base = minutos_espera(horarios, hora_actual)
    espera_total, retraso = aplicar_lluvia(espera_base)
    
    print(f"\nHora actual: {hora_actual}")
    print(f"Tiempo de espera base: {espera_base} minutos")
    if retraso > 0:
        print(f"Retraso por lluvia tropical: +{retraso} minutos")
    print(f"Tiempo de espera total: {espera_total} minutos")
    
    # Estado del sistema
    print(f"\n {bus1}")
    print(f" {parada1}")
    
    # Proceso de abordaje
    subidos = abordar_desde_parada(parada1, bus1)
    print(f"Subieron {subidos} pasajeros al bus")
    
    # Estadísticas finales
    registro = RegistroEspera()
    registro.agregar(bus1.ruta, espera_total)
    stats = registro.resumen(bus1.ruta)
    print(f"\nEstadísticas: Promedio {stats['promedio']} min, "
          f"Desviación: {stats['desv']}")


def menu_principal():
    """Menú principal interactivo"""
    while True:
        print("\nBUSPREDICT - PREDICTOR DE BUSES PANAMÁ")
        print("=" * 50)
        print("1. DEMO")
        print("2. Simulación Completa del Sistema")
        print("3. Solo ver Gráficos")
        print("4. Prueba de Algoritmos")
        print("0. Salir")
        print("-" * 50)
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            demo_espectacular()
        elif opcion == "2":
            simulacion_completa()
        elif opcion == "3":
            try:
                mostrar_graficos_demo()
            except ImportError:
                print("Instala matplotlib para ver gráficos: pip install matplotlib")
        elif opcion == "4":
            # Prueba rápida de algoritmos
            datos = [{'tiempo_total': 25}, {'tiempo_total': 15}, {'tiempo_total': 30}]
            ordenados = clasificacion_quicksort(datos, 'tiempo_total')
            print(f"Algoritmo QuickSort: {[d['tiempo_total'] for d in ordenados]}")
        elif opcion == "0":
            print("¡Gracias por usar BUSPREDICT!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()


