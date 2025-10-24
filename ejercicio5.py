import math

# Función auxiliar
def calcular_area_circulo(radio):
    """Calcula el área de un círculo con su radio."""
    return math.pi * (radio ** 2)

# Función principal
def programa_circulo():
    while True:
        print("\n=== Cálculo del área de un círculo ===")
        radio = float(input("Ingrese el radio del círculo: "))

        area = calcular_area_circulo(radio)
        print(f"\nEl área del círculo es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_circulo()
