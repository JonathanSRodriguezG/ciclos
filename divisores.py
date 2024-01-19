#Escriba un programa que entregue todos los divisores del número entero ingresado:


numero = int(input("Ingrese un numero:    "))

if numero > 0:
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    print(f"{divisores}")
else:
    print("Por favor, ingrese un número entero válido.")