# Ejercicio 38: Diseñe un algoritmo que solicite la cantidad de dinero en una cuenta y calcule el 5% de interés

def calcular_interes():
    while True:
        print("=== CÁLCULO DEL 5% DE INTERÉS DE UNA CUENTA ===")
        cantidad = float(input("Ingrese la cantidad de dinero en la cuenta: "))

        interes = cantidad * 0.05
        total = cantidad + interes

        print(f"Interés ganado: ${interes:.2f}")
        print(f"Total en la cuenta con interés: ${total:.2f}")

        opcion = input("¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_interes()
