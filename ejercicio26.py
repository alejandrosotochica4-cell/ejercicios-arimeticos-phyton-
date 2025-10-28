# Ejercicio 26: Desarrolla un programa que requiera dos números y muestre el producto de dichos valores

def multiplicar_dos_numeros():
    while True:
        print("=== PRODUCTO DE DOS NÚMEROS ===")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        producto = num1 * num2
        print(f"\nEl producto de {num1} × {num2} es: {producto:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

multiplicar_dos_numeros()
