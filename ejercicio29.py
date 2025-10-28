# Ejercicio 29: Crea un algoritmo que determine el residuo de la división entre dos números ingresados por el usuario.

def residuo_division():
    while True:
        print("=== CÁLCULO DEL RESIDUO DE UNA DIVISIÓN ===")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if num2 == 0:
            print("\nError: No se puede dividir entre cero.")
        else:
            residuo = num1 % num2
            print(f"\nEl residuo de {num1} ÷ {num2} es: {residuo}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

residuo_division()
