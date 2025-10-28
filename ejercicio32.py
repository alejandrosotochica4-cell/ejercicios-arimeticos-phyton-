# Ejercicio 32: Escribe un programa que pida un número y determine si es par o impar usando el operador de módulo (%)

def par_o_impar():
    while True:
        print("=== DETERMINAR SI UN NÚMERO ES PAR O IMPAR ===")
        numero = int(input("Ingrese un número: "))

        if numero % 2 == 0:
            print(f"\nEl número {numero} es PAR.")
        else:
            print(f"\nEl número {numero} es IMPAR.")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

par_o_impar()
