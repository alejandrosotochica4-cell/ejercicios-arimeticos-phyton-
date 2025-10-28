# Ejercicio 18: Calcular el área de un paralelogramo con base y altura especificadas

def calcular_area_paralelogramo():
    while True:
        print("=== CÁLCULO DEL ÁREA DE UN PARALELOGRAMO ===")
        base = float(input("Ingrese la base del paralelogramo: "))
        altura = float(input("Ingrese la altura del paralelogramo: "))

        area = base * altura
        print(f"\nEl área del paralelogramo es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_area_paralelogramo()
