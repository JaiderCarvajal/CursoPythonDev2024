#Ejercicio1 : Calculadora simple


#numero1 = float(input("Ingresa el primer numero: "))
#numero2 = float(input("Ingresa el segundo numero: "))
#operacion = input("Ingresa la operacion: ")

#if operacion == "+":    
#    print(f"El resultado es: {numero1 + numero2}")
#elif operacion == "-":                                      
#    print(f"El resultado es: {numero1 - numero2}")
#elif operacion == "*":
#    print(f"El resultado es: {numero1 * numero2}")
#elif operacion == "/":    
#    print(f"El resultado es: {numero1 / numero2}")
#else:
#    print("Operacion invalida")

inputUsuario = input("Ingresa un numero: ")

isNumeric = inputUsuario.isnumeric() 
isDecimal = inputUsuario.isdecimal()

