# Función auxiliar
def calcular_area_rectangulo(longitud, ancho):
    """Calcula el área de un rectángulo."""
    return longitud * ancho

# Función principal
def programa_rectangulo():
    while True:
        print("\n=== Cálculo del área de un rectángulo ===")
        longitud = float(input("Ingrese la longitud: "))
        ancho = float(input("Ingrese el ancho: "))

        area = calcular_area_rectangulo(longitud, ancho)
        print(f"\nEl área del rectángulo es: {area:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_rectangulo()
