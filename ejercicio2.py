import math

# Función auxiliar
def calcular_volumen_esfera(radio):
    """Calcula el volumen de una esfera con su radio dado."""
    return (4/3) * math.pi * (radio ** 3)

# Función principal
def programa_esfera():
    while True:
        print("\n=== Cálculo del volumen de una esfera ===")
        radio = float(input("Ingrese el radio de la esfera: "))

        volumen = calcular_volumen_esfera(radio)
        print(f"\nEl volumen de la esfera es: {volumen:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_esfera()
