def contar_palabra(texto, palabra): # Se le agragaron los dos puntos al final, para poder tener la sintaxis correcta de la función
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

print(f"La palabra '{palabra_buscada} aparece {contar_palabra(texto, palabra_buscada)} veces.") # Se organizaron los corchetes para la variable: 
                                                                                                # "palabra_buscada", y para la función:
                                                                                                # "contar_palabra"      
