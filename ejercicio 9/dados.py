import random # se corrigio la palabra random

def simular_lanzamiento_dados(cantidad_dados, caras_por_dado):
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    return resultados # se corrigio la palabra return

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado) # se añadio el argumento cantidad_dados
print(f"Resultados del lanzamiento: {lanzamientos}")

