# Calcular el área de un trapecio
while True:
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))

    area = ((base_mayor + base_menor) * altura) / 2
    print("El área del trapecio es:", area)

    repetir = input("¿Desea realizar otro cálculo? (s/n): ").lower()
    if repetir!= "s":
            print("Saliendo del programa..."
            break
        
