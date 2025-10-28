# Ejercicio 21: Calcular el área de un hexágono regular con la longitud de su lado especificada

import math

def calcular_area_hexagono():
    while True:
        print("=== CÁLCULO DEL ÁREA DE UN HEXÁGONO REGULAR ===")
        lado = float(input("Ingrese la longitud del lado del hexágono: "))

        area = (3 * math.sqrt(3) * (lado ** 2)) / 2
        print(f"\nEl área del hexágono es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_area_hexagono()
