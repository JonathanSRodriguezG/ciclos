def collsecuenciea(n):
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        secuencia.append(n)
    return secuencia

numero = int(input("Ingrese un número entero para generar la secuencia de Collatz: "))
imprimir = collsecuenciea(numero)

print(f"Secuencia de Collatz para {numero}: ")
print(f"{imprimir}")
