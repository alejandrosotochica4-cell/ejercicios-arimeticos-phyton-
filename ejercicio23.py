# Ejercicio 23: Convertir litros a galones

def convertir_litros_a_galones():
    while True:
        print("=== CONVERSIÓN DE LITROS A GALONES ===")
        litros = float(input("Ingrese la cantidad en litros: "))

        galones = litros * 0.264172
        print(f"\n{litros:.2f} litros equivalen a {galones:.4f} galones.")

        opcion = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

convertir_litros_a_galones()
