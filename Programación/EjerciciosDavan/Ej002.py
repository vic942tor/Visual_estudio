# Ejercicio 02: El mismo ejercicio anterior pero ahora el diccionario, comienza siendoundiccionariovacío, al que sólo se 
# le agregan como elementos las letras que están en la frase. El restodeletrasque no están en la frase no están en el diccionario.

# Pedimos al usuario que introduzca la frase
frase = input("Introduce una frase: ")

# Convertimos la frase a minúsculas y eliminamos los espacios
frase = frase.lower().replace(" ", "")

# Inicializamos un diccionario vacío
diccionario_letras = {}

# Recorremos cada carácter de la frase
for caracter in frase:
    if caracter.isalpha():  # Verificamos que sea una letra
        if caracter in diccionario_letras:
            diccionario_letras[caracter] += 1
        else:
            diccionario_letras[caracter] = 1

# Buscamos las letras más repetidas
max_repeticiones = max(diccionario_letras.values())
letras_mas_repetidas = [letra for letra, valor in diccionario_letras.items() if valor == max_repeticiones]

# Buscamos las letras menos repetidas
min_repeticiones = min(diccionario_letras.values())
letras_menos_repetidas = [letra for letra, valor in diccionario_letras.items() if valor == min_repeticiones]

# Mostramos los resultados
print("Diccionario de frecuencias:", diccionario_letras)
print("Letras más repetidas:", letras_mas_repetidas, "con", max_repeticiones, "repeticiones.")
print("Letras menos repetidas:", letras_menos_repetidas, "con", min_repeticiones, "repeticiones.")
