# Ejercicio 27: Diseña un algoritmo que pida un número y calcule su cuadrado utilizando el operador de multiplicación

def calcular_cuadrado():
    while True:
        print("=== CÁLCULO DEL CUADRADO DE UN NÚMERO ===")
        numero = float(input("Ingrese un número: "))

        cuadrado = numero * numero
        print(f"\nEl cuadrado de {numero} es: {cuadrado:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_cuadrado()
