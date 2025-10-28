# Ejercicio 36: Crea un algoritmo que solicite una distancia en kilómetros y la convierta en millas

def convertir_kilometros_a_millas():
    while True:
        print("=== CONVERSIÓN DE KILÓMETROS A MILLAS ===")
        kilometros = float(input("Ingrese la distancia en kilómetros: "))

        millas = kilometros * 0.621371
        print(f"\n{kilometros} kilómetros equivalen a {millas:.2f} millas.")

        opcion = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

convertir_kilometros_a_millas()
