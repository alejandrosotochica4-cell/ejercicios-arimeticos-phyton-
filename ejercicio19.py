# Ejercicio 19: Determinar el volumen de un cubo con la longitud de su lado especificada

def calcular_volumen_cubo():
    while True:
        print("=== CÁLCULO DEL VOLUMEN DE UN CUBO ===")
        lado = float(input("Ingrese la longitud del lado del cubo: "))

        volumen = lado ** 3
        print(f"\nEl volumen del cubo es: {volumen:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_volumen_cubo()
