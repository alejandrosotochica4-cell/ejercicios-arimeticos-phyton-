# Ejercicio 33: Crea un algoritmo que solicite el radio de un círculo y calcule su circunferencia

def circunferencia_circulo():
    while True:
        print("=== CÁLCULO DE LA CIRCUNFERENCIA DE UN CÍRCULO ===")
        radio = float(input("Ingrese el radio del círculo: "))

        circunferencia = 2 * 3.1416 * radio
        print(f"\nLa circunferencia del círculo es: {circunferencia:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

circunferencia_circulo()
