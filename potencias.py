# Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

n = int(input("Ingrese hasta que potencia de dos quiere ver:\n "))
for i in range(n+1):
    resultado= 2**i
    print(resultado, end=" ")
    
