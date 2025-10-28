# Ejercicio 39: Escriba un programa que pida dos números enteros y muestre el cociente de la división entera

def division_entera():
    while True:
        print("=== CÁLCULO DEL COCIENTE DE LA DIVISIÓN ENTERA ===")
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))

        if num2 == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            cociente = num1 // num2
            print(f"\nEl cociente de la división entera es: {cociente}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

division_entera()
