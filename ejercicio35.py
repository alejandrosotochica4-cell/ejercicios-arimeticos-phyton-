# Ejercicio 35: Diseñe un algoritmo que calcule el área de un rectángulo solicitando su longitud y ancho

def area_rectangulo():
    while True:
        print("=== CÁLCULO DEL ÁREA DE UN RECTÁNGULO ===")
        longitud = float(input("Ingrese la longitud del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))

        area = longitud * ancho
        print(f"\nEl área del rectángulo es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

area_rectangulo()
