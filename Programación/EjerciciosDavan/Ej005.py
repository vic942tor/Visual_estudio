# Ejercicio 05: Realizar un programa que mediante un diccionario asocie a cada letra el númerodeveces que aparece en una frase como la primera letra de una palabra.

# Pedimos al usuario que introduzca la frase
frase = input("Introduce una frase: ")

# Convertimos la frase a minúsculas
frase = frase.lower()

# Dividimos la frase en palabras
palabras = frase.split()

# Inicializamos un diccionario vacío
diccionario_primera_letra = {}

# Recorremos cada palabra
for palabra in palabras:
    primera_letra = palabra[0]  # Obtenemos la primera letra de la palabra
    if primera_letra.isalpha():  # Verificamos que sea una letra
        if primera_letra in diccionario_primera_letra:
            diccionario_primera_letra[primera_letra] += 1
        else:
            diccionario_primera_letra[primera_letra] = 1

# Ordenamos el diccionario por las claves (letras) en orden alfabético
diccionario_ordenado = dict(sorted(diccionario_primera_letra.items()))

# Mostramos el diccionario ordenado
print("Número de veces que cada letra aparece como primera letra de una palabra (orden alfabético):")
for letra, ocurrencias in diccionario_ordenado.items():
    print(f"{letra}: {ocurrencias}")

