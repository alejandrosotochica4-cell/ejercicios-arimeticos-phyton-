# Ejercicio 20: Convertir libras a kilogramos

def convertir_libras_a_kilogramos():
    while True:
        print("=== CONVERSIÓN DE LIBRAS A KILOGRAMOS ===")
        libras = float(input("Ingrese la cantidad en libras: "))

        kilogramos = libras * 0.453592
        print(f"\n{libras} libras equivalen a {kilogramos:.2f} kilogramos.")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

convertir_libras_a_kilogramos()

