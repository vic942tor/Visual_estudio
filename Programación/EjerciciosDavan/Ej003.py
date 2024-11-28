# Ejercicio 03: El mismo ejercicio que 1, pero ahora el diccionario se crea de la siguienteforma:
# {ocurrencia: lista_letra}
# ocurrencia: es un número entero n que representa que la letras de la lista aparecennvecesenlafrase.
# lista_letra: es una lista que contiene las letras que aparecen “ocurrencia” veces en el texto. Inicialmente, 
# para facilitar la respuesta de la pregunta 3, el diccionario tiene el siguientenodo:
# {0, [todas las letras del abecedario como elementos de la lista]}

# Inicializamos el diccionario con todas las letras del abecedario en la lista de ocurrencia 0
diccionario_ocurrencias = {0: [chr(letra) for letra in range(ord('a'), ord('z') + 1)]}

# Pedimos al usuario que introduzca la frase
frase = input("Introduce una frase: ")

# Convertimos la frase a minúsculas y eliminamos los espacios
frase = frase.lower().replace(" ", "")

# Recorremos cada carácter de la frase
for caracter in frase:
    if caracter.isalpha():  # Verificamos que sea una letra
        # Eliminamos la letra de la lista en 0 si está allí
        if caracter in diccionario_ocurrencias[0]:
            diccionario_ocurrencias[0].remove(caracter)
        
        # Buscamos la ocurrencia actual de la letra
        ocurrencia_actual = next((key for key, letras in diccionario_ocurrencias.items() if caracter in letras), None)
        
        if ocurrencia_actual is not None:  # Si ya existe, movemos la letra al siguiente nivel
            diccionario_ocurrencias[ocurrencia_actual].remove(caracter)
            nueva_ocurrencia = ocurrencia_actual + 1
        else:  # Si no existe, es la primera vez que la encontramos
            nueva_ocurrencia = 1
        
        # Añadimos la letra en su nueva ocurrencia
        if nueva_ocurrencia not in diccionario_ocurrencias:
            diccionario_ocurrencias[nueva_ocurrencia] = []
        diccionario_ocurrencias[nueva_ocurrencia].append(caracter)

# Eliminamos las claves con listas vacías
diccionario_ocurrencias = {key: letras for key, letras in diccionario_ocurrencias.items() if letras}

# Buscamos las ocurrencias máximas y mínimas
max_ocurrencia = max(diccionario_ocurrencias.keys())
min_ocurrencia = min(diccionario_ocurrencias.keys())

# Mostramos los resultados
print("Diccionario de ocurrencias:", diccionario_ocurrencias)
print("Letras más repetidas:", diccionario_ocurrencias[max_ocurrencia], "con", max_ocurrencia, "repeticiones.")
print("Letras menos repetidas:", diccionario_ocurrencias[min_ocurrencia], "con", min_ocurrencia, "repeticiones.")
print("Letras no usadas:", diccionario_ocurrencias.get(0, []))
