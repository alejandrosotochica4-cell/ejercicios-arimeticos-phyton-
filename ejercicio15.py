# Ejercicio 15: Calcular el área de un cuadrado con el lado dado

def calcular_area_cuadrado():
    while True:
        print("=== CÁLCULO DEL ÁREA DE UN CUADRADO ===")
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))

        area = lado ** 2
        print(f"\nEl área del cuadrado es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_area_cuadrado()
