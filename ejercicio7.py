# ------------------ Convertir grados Celsius a Fahrenheit ------------------

# Función auxiliar
def convertir_celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

# Función principal
def programa_celsius_fahrenheit():
    while True:
        print("\n=== Conversión de grados Celsius a Fahrenheit ===")
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))

        fahrenheit = convertir_celsius_a_fahrenheit(celsius)
        print(f"\n{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")

        opcion = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_celsius_fahrenheit()
