#import math

#resultado = math.sqrt(16)

#print(f"El resultado es: {resultado}")

#edad = int(input("Ingresa tu edad: "))
#if edad >= 18:
#print("Eres mayor de edad")
#elif edad >= 13:
#    print("Eres adolescente")
#else:
#    print("Eres un niño")
#Bucle for conociendo la cantidad de veces que se repite el codigo
#for i in range(0,10,2):
#    print(i)

contador = 1

while contador:
    print(f"Este es el númer {contador*2}")
    contador += 1

    if contador >= 1000:
        break