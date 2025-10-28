# Ejercicio 37: Desarrolla un programa que pida el precio de un artículo y calcule el 10% de descuento

def calcular_descuento():
    while True:
        print("=== CÁLCULO DEL 10% DE DESCUENTO DE UN ARTÍCULO ===")
        precio = float(input("Ingrese el precio del artículo: "))

        descuento = precio * 0.10
        precio_final = precio - descuento

        print(f"\nDescuento aplicado: ${descuento:.2f}")
        print(f"Precio final con descuento: ${precio_final:.2f}")

        opcion = input("\n¿Desea calcular otro descuento? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_descuento()
