#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
total = 0

while True:
    duraciontramo= int(input("Ingrese la duración del tramo:"))
    
    if duraciontramo == 0:
        break
    total += duraciontramo

hora = total //60
minutos = total %60
print(f"Tiempo total del viaje: {hora}:{minutos} horas")