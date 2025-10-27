# ------------------ Calcular el área de un trapecio ------------------

# Función auxiliar
def calcular_area_trapecio(base_mayor, base_menor, altura):
    """Calcula el área de un trapecio a partir de sus bases y altura."""
    return ((base_mayor + base_menor) * altura) / 2

# Función principal
def programa_trapecio():
    while True:
        print("\n=== Cálculo del área de un trapecio ===")
        base_mayor = float(input("Ingrese la base mayor: "))
        base_menor = float(input("Ingrese la base menor: "))
        altura = float(input("Ingrese la altura: "))

        area = calcular_area_trapecio(base_mayor, base_menor, altura)
        print(f"\nEl área del trapecio es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_trapecio()
