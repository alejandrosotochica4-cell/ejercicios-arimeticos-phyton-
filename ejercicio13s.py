# Ejercicio 12: Calcular el área de un trapecio con sus longitudes de bases y altura especificadas

def calcular_area_trapecio():
    while True:
        print("=== CÁLCULO DEL ÁREA DE UN TRAPECIO ===")
        base_mayor = float(input("Ingrese la longitud de la base mayor: "))
        base_menor = float(input("Ingrese la longitud de la base menor: "))
        altura = float(input("Ingrese la altura del trapecio: "))

        area = ((base_mayor + base_menor) * altura) / 2
        print(f"\nEl área del trapecio es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_area_trapecio()
