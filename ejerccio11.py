# ------------------ Convertir kilómetros a millas ------------------

# Función auxiliar
def convertir_kilometros_a_millas(kilometros):
    """Convierte kilómetros a millas."""
    return kilometros * 0.621371

# Función principal
def programa_kilometros_millas():
    while True:
        print("\n=== Conversión de kilómetros a millas ===")
        kilometros = float(input("Ingrese la distancia en kilómetros: "))

        millas = convertir_kilometros_a_millas(kilometros)
        print(f"\n{kilometros:.2f} km equivalen a {millas:.2f} millas")

        opcion = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_kilometros_millas()
