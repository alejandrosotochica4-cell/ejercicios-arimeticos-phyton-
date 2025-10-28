# Ejercicio 25: Crea un algoritmo que pida al usuario dos números y calcule la resta del primero menos el segundo

def restar_dos_numeros():
    while True:
        print("=== RESTA DE DOS NÚMEROS ===")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resta = num1 - num2
        print(f"\nLa resta de {num1} - {num2} es: {resta:.2f}")

        opcion = input("\n¿Desea realizar otra resta? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

restar_dos_numeros()
