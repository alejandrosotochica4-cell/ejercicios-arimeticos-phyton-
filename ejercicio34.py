# Ejercicio 34: Escribe un programa que convierta una cantidad de horas ingresadas por el usuario a minutos

def convertir_horas_a_minutos():
    while True:
        print("=== CONVERSIÓN DE HORAS A MINUTOS ===")
        horas = float(input("Ingrese la cantidad de horas: "))

        minutos = horas * 60
        print(f"\n{horas} horas equivalen a {minutos:.2f} minutos.")

        opcion = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

convertir_horas_a_minutos()
