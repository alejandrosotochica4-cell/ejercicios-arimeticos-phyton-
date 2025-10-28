# Ejercicio 17: Convertir pulgadas a centímetros

def convertir_pulgadas_a_centimetros():
    while True:
        print("=== CONVERSIÓN DE PULGADAS A CENTÍMETROS ===")
        pulgadas = float(input("Ingrese la cantidad en pulgadas: "))

        centimetros = pulgadas * 2.54
        print(f"\n{pulgadas} pulgadas equivalen a {centimetros:.2f} centímetros.")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

convertir_pulgadas_a_centimetros()
