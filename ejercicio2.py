#Ejercicio 2: Conversión de Unidades
#Crea un programa que convierta una medida en metros 
#a centímetros y milímetros. 
# El programa debe pedir al usuario que ingrese una 
# longitud en metros y luego mostrar el resultado en las 
# dos unidades.


    
numeroMetros = 0

while numeroMetros == 0:
    #Pedimos al usuario que ingrese el número a convertir
    numeroMetros = input("Ingresa un numero o escriba salir para terminar: ")
    if numeroMetros == "salir":
        break
    else:
        numeroMetros = float(numeroMetros)
    #Convertimos los metros a centimetros y milimetros
    centimetros = numeroMetros * 100
    milimetros = numeroMetros * 1000

    #Mostramos los resultados
    print(f"El número ingresado en centimetros es {centimetros} y en milimetros es {milimetros}")

    numeroMetros = 0


    

   
