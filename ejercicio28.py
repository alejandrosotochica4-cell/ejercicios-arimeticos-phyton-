# Ejercicio 28: Escriba un programa que solicite dos números y calcule la división del primero entre el segundo

def dividir_dos_numeros():
    while True:
        print("=== DIVISIÓN DE DOS NÚMEROS ===")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if num2 == 0:
            print("\nError: No se puede dividir entre cero.")
        else:
            division = num1 / num2
            print(f"\nEl resultado de {num1} ÷ {num2} es: {division:.2f}")

        opcion = input("\n¿Desea realizar otra división? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

dividir_dos_numeros()
