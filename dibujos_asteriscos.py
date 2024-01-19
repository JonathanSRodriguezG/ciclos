#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos
#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:
#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

def dibujar_rectangulo():
    altura = int(input("Ingrese la altura: "))
    ancho = int(input("Ingrese el ancho: "))

    for i in range(altura):
            print("*" * ancho)
        
def dibujar_triangulo():
    altura = int(input("Ingrese la altura: "))

    for i in range(1, altura + 1):
     print("*" * i)
    
def dibujar_hexagono():
    lado = int(input("Ingrese el tamaño del lado del hexágono: "))

    for i in range(lado):
        espacios = " " * (lado - i - 1)
        asteriscos = "*" * (2 * i + 1)
        print(espacios + asteriscos)
    for i in range(lado - 2, -1, -1):
        espacios = " " * (lado - i - 1)
        asteriscos = "*" * (2 * i + 1)
        print(espacios + asteriscos)

def main():
    opcion = input("Elija la figura a dibujar (rectangulo/triangulo/hexagono): ")

    if opcion.lower() == "rectangulo":
        dibujar_rectangulo()
    elif opcion.lower() == "triangulo":
        dibujar_triangulo()
    elif opcion.lower() == "hexagono":
        dibujar_hexagono()
    else:
        print("Opción no válida. Por favor, elija entre rectangulo, triangulo o hexagono.")

if __name__ == "__main__":
    main()