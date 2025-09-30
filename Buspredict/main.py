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


def main():
    # Crear un bus con horarios
    horarios = ["07:00", "07:15", "07:30"]
    bus1 = Bus(bus_id=1, ruta="Via España", capacidad=3, horario=horarios)
    parada1 = Parada("Estación Central")

    # --- Pasajeros en la parada ---
    pasajeros_base = 2
    pasajeros_final = aplicar_factor_quincena(pasajeros_base)  # aumenta en quincena
    print(f"Pasajeros base: {pasajeros_base}")
    if pasajeros_final > pasajeros_base:
        print(f"⚠️ Factor quincena aplicado → Pasajeros ahora: {pasajeros_final}")
    else:
        print(f"Pasajeros finales: {pasajeros_final}")

    for i in range(pasajeros_final):
        parada1.agregar_pasajero(Pasajero(i+1, f"Destino {i+1}", "06:55"))

    # --- Predicción del próximo bus ---
    hora_actual = "07:10"
    idx, prox_bus = busqueda_binaria(horarios, hora_actual)
    espera_base = minutos_espera(horarios, hora_actual)

    # Aplicar lluvia tropical
    espera_total, retraso = aplicar_lluvia(espera_base)

    print(f"\nHora actual: {hora_actual}")
    if prox_bus:
        print(f"Próximo bus programado: {prox_bus}")
        print(f"Tiempo de espera base: {espera_base} minutos")
        if retraso > 0:
            print(f"Retraso por lluvia tropical: +{retraso} minutos ☔")
        print(f"Tiempo de espera total: {espera_total} minutos\n")
    else:
        print("No hay más buses hoy.\n")

    # --- Estado inicial ---
    print(bus1)
    print(parada1)

    # --- Subir pasajeros al bus ---
    subidos = abordar_desde_parada(parada1, bus1)
    print(f"Subieron {subidos} pasajeros al {bus1}")

    # --- Estadísticas de espera ---
    registro = RegistroEspera()
    registro.agregar(bus1.ruta, espera_total)
    print("\nEstadísticas de espera:", registro.todas())


if __name__ == "__main__":
    main()


