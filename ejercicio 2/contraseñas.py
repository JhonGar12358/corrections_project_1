import random # se corrigio el nombre rando a random, para poder importar bien la funcion
import string

def generar_contraseña(longitud=8): # se corrigio la sintaxis de la funcion, ya que le falta la palabra clave "def" antes del nombre de la función
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña # se corrigio la palabra return

print(generar_contraseña()) # se corrigio la funcion, por que se estaba escribiendo con n, y esta escrita con ñ. asi que por eso aparecia indefinida, o desconocida
