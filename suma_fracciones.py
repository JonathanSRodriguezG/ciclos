potencia=1
fraccion=0.5
suma=0
print("Potencia\tFraccion\tSuma")
print(f"{potencia}\t\t{fraccion}\t\t{suma}")
while fraccion > 0.000001:
    potencia += 1
    fraccion /= 2
    suma += fraccion
    print(f"{potencia}\t\t{fraccion}\t\t{suma}")