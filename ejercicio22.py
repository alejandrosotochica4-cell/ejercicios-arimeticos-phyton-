# Ejercicio 22: Determinar el volumen de un prisma triangular

def calcular_volumen_prisma_triangular():
    while True:
        print("=== CÁLCULO DEL VOLUMEN DE UN PRISMA TRIANGULAR ===")
        base = float(input("Ingrese la base del triángulo (cm): "))
        altura_triangulo = float(input("Ingrese la altura del triángulo (cm): "))
        longitud_prisma = float(input("Ingrese la longitud del prisma (cm): "))

        area_base = (base * altura_triangulo) / 2
        volumen = area_base * longitud_prisma

        print(f"\nEl volumen del prisma triangular es: {volumen:.2f} cm³")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_volumen_prisma_triangular()
