# Ejercicio 06: Realizar un programa que mediante un diccionario almacene las palabrasenfunciónde su longitud. Después escribir de forma decreciente en longitud:
# Longitud n:
# palabra01 palabra02 palabra03
# Longitud n-1:
# palabra01 palabra02 palabra03
# .
# .
# .Longitud 1:
# palabra01 palabra02 palabra03

# Pedimos al usuario que introduzca la frase
frase = input("Introduce una frase: ")

# Dividimos la frase en palabras
palabras = frase.split()

# Inicializamos un diccionario vacío
diccionario_longitud = {}

# Recorremos cada palabra
for palabra in palabras:
    longitud = len(palabra)  # Calculamos la longitud de la palabra
    if longitud in diccionario_longitud:
        diccionario_longitud[longitud].append(palabra)
    else:
        diccionario_longitud[longitud] = [palabra]

# Ordenamos las longitudes en orden decreciente
longitudes_ordenadas = sorted(diccionario_longitud.keys(), reverse=True)

# Mostramos las palabras agrupadas por longitud
print("Palabras agrupadas por longitud (de mayor a menor):")
for longitud in longitudes_ordenadas:
    palabras_con_longitud = " ".join(diccionario_longitud[longitud])
    print(f"Longitud {longitud}:")
    print(palabras_con_longitud)
