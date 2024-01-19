#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

n = int(input("Ingrese un numero del 1 al 10 para ver su tabla: "))
for i in range(10):
    print(f"{n} * {i+1} = {n*(i+1)}")
