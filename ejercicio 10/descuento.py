def calcular_precio_con_descuento(precio_base, porcentaje_descuento): #secorrigio el nombre de la funcion la palabra descuento, se añadio el def, y los dos puntos
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento
    return precio_final

precio_base = float(input("Ingrese el precio base del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
