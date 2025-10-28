# Ejercicio 31: Diseña un algoritmo que solicite la base y la altura de un triángulo y calcule su área

def area_triangulo():
    while True:
        print("=== CÁLCULO DEL ÁREA DE UN TRIÁNGULO ===")
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))

        area = (base * altura) / 2
        print(f"\nEl área del triángulo es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

area_triangulo()
