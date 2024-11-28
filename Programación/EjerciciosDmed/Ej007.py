# Dada una lista de palabras, agrúpelas por su letra inicial a través de un diccionario de
# listas. Escriba un programa en Python que cree el diccionario y luego muestre las
# palabras en orden alfabético. 

# Lista de palabras
palabras = ["manzana", "mango", "banana", "pera", "ciruela", "cereza", "melon", "mandarina"]

# Diccionario para agrupar las palabras por la letra inicial
grupo_palabras = {}

# Agrupar las palabras por su letra inicial
for palabra in palabras:
    letra_inicial = palabra[0].lower()  # Tomamos la primera letra y la pasamos a minúsculas
    if letra_inicial not in grupo_palabras:
        grupo_palabras[letra_inicial] = []
    grupo_palabras[letra_inicial].append(palabra)

# Mostrar las palabras en orden alfabético dentro de cada grupo
print("Palabras agrupadas por letra inicial:")
for letra, lista_palabras in sorted(grupo_palabras.items()):  # Ordenamos las letras del diccionario
    lista_palabras.sort()  # Ordenamos las palabras alfabéticamente dentro del grupo
    print(f"{letra.upper()}: {', '.join(lista_palabras)}")

