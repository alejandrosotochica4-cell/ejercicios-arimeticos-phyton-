# Ejercicio 30: Desarrolla un programa que pida un número y calcule su raíz cuadrada utilizando operadores aritméticos

def raiz_cuadrada():
    while True:
        print("=== CÁLCULO DE LA RAÍZ CUADRADA ===")
        numero = float(input("Ingrese un número: "))

        if numero < 0:
            print("\nError: No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            # La raíz cuadrada se calcula como el número elevado a la potencia 0.5
            raiz = numero ** 0.5
            print(f"\nLa raíz cuadrada de {numero} es: {raiz:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

raiz_cuadrada()
