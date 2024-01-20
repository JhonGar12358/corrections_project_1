# se crea una funcion de nombre calculadora()
def calculadora():
# se crea una variable tipo float para recibir el primer numero a operar
    num1 = float(input("Ingrese el primer número: ")) # se corrigio, agregando el input en la variable para que pueda ser una entra para el usuario
# se crea una variable tipo float para recibir el segundo numero a operar
    num2 = float(input("Ingrese el segundo número: ")) # se corrigio, agregando el input en la variable para que pueda ser una entra para el usuario
# se crea una variable tipo input para que el usuario ingrese el tipo de operacion que desea realizar
    operacion = input("Ingrese la operación (+, -, *, /): ")
# se crea un condicional if para la operacion sumar
    if operacion == '+':
        # se crea una variable local "resultado" donde suman las variables a operar
        resultado = num1 + num2 #se corrigio la variable num a num1, para que la pueda reconocer
# se crea un condicional elif para la operacion restar
    elif operacion == '-':
        # se crea una variable local "resultado" donde restan las variables a operar
        resultado = num1 - num2
# se crea un condicional elif para la operacion multiplicar
    elif operacion == '*':
        # se crea una variable local "resultado" donde multiplican las variables a operar
        resultado = num1 * num2
        
# se crea un condicional elif para la operacion dividir
    elif operacion == '/':
        # se crea una variable local "resultado" donde dividen las variables a operar
        resultado = num1 / num2 #se corrigio la variable num a num1, para que la pueda reconocer
# se crea un condicional de descarte elif para el caso en el se ingrese un caracter diferente
    else:
        resultado = "Operación no válida"

    print("Resultado: ",resultado) # se corrigio el print, al añadir la coma (,) antes de la variable resultado, para asi poder contatenar la misma.

calculadora() # se corrigio el nombre de la funcion de "calculdora()" a "calculadora()", le faltaba una a para poder llamar correctamente la funcion.
