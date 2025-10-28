# Ejercicio 24: Escribe un programa que solicite dos números al usuario y muestre la suma de ambos

def sumar_dos_numeros():
    while True:
        print("=== SUMA DE DOS NÚMEROS ===")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        suma = num1 + num2
        print(f"\nLa suma de {num1} + {num2} es: {suma:.2f}")

        opcion = input("\n¿Desea realizar otra suma? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

sumar_dos_numeros()
