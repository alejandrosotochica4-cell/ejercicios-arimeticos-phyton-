# ------------------ Calcular volumen de un prisma rectangular ------------------

# Función auxiliar
def calcular_volumen_prisma(longitud, ancho, altura):
    """Calcula el volumen de un prisma rectangular."""
    return longitud * ancho * altura

# Función principal
def programa_prisma_rectangular():
    while True:
        print("\n=== Cálculo del volumen de un prisma rectangular ===")
        longitud = float(input("Ingrese la longitud: "))
        ancho = float(input("Ingrese el ancho: "))
        altura = float(input("Ingrese la altura: "))

        volumen = calcular_volumen_prisma(longitud, ancho, altura)
        print(f"\nEl volumen del prisma rectangular es: {volumen:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del programa...")
            break

programa_prisma_rectangular()
