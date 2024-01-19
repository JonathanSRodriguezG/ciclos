n = int(input("Ingrese el número de términos (n): "))

suma = 0
signo = 1

for i in range(1, 2 * n + 1, 2):
    termino = 4 * signo / i
    suma += termino
    signo *= -1

print(f"La estimación de π con {n} términos es: {suma}")