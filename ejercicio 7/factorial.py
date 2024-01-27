def factorial(n): # Se corrigen y añaden los dos puntos para que ejecute la funcion
    if n == 0 or n == 1: # se añade un igual (=) para que la comparacion sea valida y se ponen los dos puntos al final
        return 1 # se corrigio la palabra return
    else:
        return n * factorial(n - 1) # se corrigio la palabra return

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")
