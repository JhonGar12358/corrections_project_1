def celsius_a_fahrenheit(celsius):# Se le agragaron los dos puntos al final, para poder tener la sintaxis correcta de la función
    return (celsius * 9/5) + 32 # Se le añadio el operador + para completar la formula de conversión 

temperatura_celsius = float(input("Ingrese la temperatura en Celsius: ")) # se corrigio, agregando el input en la variable para que pueda ser una entra para el usuario
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
