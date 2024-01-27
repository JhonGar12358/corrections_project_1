def es_palindromo(texto): # Se le agragaron los dos puntos al final, para poder tener bien la sintaxis correcta de la función
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto == texto[::-1]

palabra_frase = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra_frase): # se añadio el argumento necesario para que la funcion valide si la palabra ingresada es palindroma.
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")
