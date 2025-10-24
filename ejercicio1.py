# ------------------ Calcular el área de un triángulo ------------------

# Función auxiliar: realiza el cálculo
def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo con base y altura dadas."""
    return (base * altura) / 2

# Función principal: controla el flujo del programa
def programa_triangulo():
    while True:
        print("\n=== Cálculo del área de un triángulo ===")
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))

        area = calcular_area_triangulo(base, altura)
        print(f"\nEl área del triángulo es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

# Programa principal
programa_triangulo()
