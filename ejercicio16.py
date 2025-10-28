# Ejercicio 16: Determinar el volumen de una pirámide con longitud de la base, ancho de la base y altura especificadas

def calcular_volumen_piramide():
    while True:
        print("=== CÁLCULO DEL VOLUMEN DE UNA PIRÁMIDE ===")
        longitud_base = float(input("Ingrese la longitud de la base: "))
        ancho_base = float(input("Ingrese el ancho de la base: "))
        altura = float(input("Ingrese la altura de la pirámide: "))

        volumen = (longitud_base * ancho_base * altura) / 3
        print(f"\nEl volumen de la pirámide es: {volumen:.2f}")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del programa...")
            break

calcular_volumen_piramide()
