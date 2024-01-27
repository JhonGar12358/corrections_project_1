def es_primo(numero):# Se le agragaron los dos puntos al final, para poder tener la sintaxis correcta de la función
    if numero < 2:# Se le agragaron los dos puntos al final, para poder tener la sintaxis correcta de la condición
        return False
    for i in range(2, int(numero**0.5) + 1):# Se le agragaron los dos puntos al final, para poder tener la sintaxis correcta del ciclo
        if numero % i == 0:# Se le agragaron los dos puntos al final, para poder tener la sintaxis correcta de la condición
            return False # Se corrigio la palabra return 
    return True # Se corrigio la palabra return

limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo(limite)]
print("Números primos:", primos)
