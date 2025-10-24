import math

# Función auxiliar
def calcular_volumen_cono(radio, altura):
    """Calcula el volumen de un cono."""
    return (1/3) * math.pi * (radio ** 2) * altura

# Función principal
def programa_cono():
    while True:
        print("\n=== Cálculo del volumen de un cono ===")
        radio = float(input("Ingrese el radio de la base: "))
        altura = float(input("Ingrese la altura: "))

        volumen = calcular_volumen_cono(radio, altura)
        print(f"\nEl volumen del cono es: {volumen:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_cono()
