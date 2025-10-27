# ------------------ Convertir dólares a euros ------------------

# Función auxiliar
def convertir_dolares_a_euros(dolares, tasa):
    """Convierte una cantidad en dólares a euros según la tasa de cambio."""
    return dolares * tasa

# Función principal
def programa_dolares_euros():
    while True:
        print("\n=== Conversión de dólares a euros ===")
        dolares = float(input("Ingrese la cantidad en dólares: "))
        tasa = float(input("Ingrese la tasa de cambio (1 dólar = cuántos euros): "))

        euros = convertir_dolares_a_euros(dolares, tasa)
        print(f"\n${dolares:.2f} USD equivalen a €{euros:.2f} EUR")

        opcion = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_dolares_euros()
