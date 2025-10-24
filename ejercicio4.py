import math

# Función auxiliar
def calcular_volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro."""
    return math.pi * (radio ** 2) * altura

# Función principal
def programa_cilindro():
    while True:
        print("\n=== Cálculo del volumen de un cilindro ===")
        radio = float(input("Ingrese el radio de la base: "))
        altura = float(input("Ingrese la altura: "))

        volumen = calcular_volumen_cilindro(radio, altura)
        print(f"\nEl volumen del cilindro es: {volumen:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_cilindro()
