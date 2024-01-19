def collsecuencia(n):
    largo = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        largo += 1
    return largo

numero = int(input("Ingrese un número entero para establecer el límite superior: "))

for num in range(1, numero+1):
    largo = collsecuencia(num)
    print(f"{num} {'*' * largo}")