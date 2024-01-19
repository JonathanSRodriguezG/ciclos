import math
eaprox = 0
n = 0  

while True:
    termino_actual = 1/math.factorial(n)
    eaprox += termino_actual

    if n > 0 and termino_actual / math.factorial(n - 1) < 0.0001:
        break

    n += 1
print(f"Valor aproximado de e: {eaprox}")