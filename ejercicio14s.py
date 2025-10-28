# Ejercicio 14: Convertir kilómetros a millas

def convertir_kilometros_a_millas():
    while True:
        print("=== CONVERSIÓN DE KILÓMETROS A MILLAS ===")
        kilometros = float(input("Ingrese la cantidad en kilómetros: "))

        millas = kilometros * 0.621371
        print(f"\n{kilometros} kilómetros equivalen a {millas:.2f} millas.")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

convertir_kilometros_a_millas()
