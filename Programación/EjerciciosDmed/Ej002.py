# Escriba un programa en Python que mediante un diccionario cuente el número de
# veces que aparece una letra en una frase leída.
# Una vez creado el diccionario se debe recorrer para mostrar por línea el número de
# ocurrencia de cada letra. 

# Pedir al usuario que ingrese una frase
frase = input("Introduce una frase: ")

# Crear un diccionario vacío para contar las letras
diccionario_letras = {}

# Recorrer cada caracter de la frase
for letra in frase:
    if letra.isalpha():  # Verificar si es una letra
        letra = letra.lower()  # Convertir la letra a minúscula para no distinguir entre mayúsculas y minúsculas
        if letra in diccionario_letras:
            diccionario_letras[letra] += 1  # Aumentar el contador si la letra ya está en el diccionario
        else:
            diccionario_letras[letra] = 1  # Añadir la letra al diccionario si es la primera vez que aparece

# Recorrer el diccionario y mostrar el número de ocurrencias de cada letra
print("\nNúmero de ocurrencias de cada letra:")
for letra, ocurrencias in diccionario_letras.items():
    print(f"{letra}: {ocurrencias}")
