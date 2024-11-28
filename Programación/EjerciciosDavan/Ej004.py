# Ejercicio 04: Teniendo como base el ejercicio 1, modificar el programa para que muestreordenadasde mayor a menor las ocurrencia de letras de la frase leída.

# Inicializamos el diccionario con todas las letras del abecedario en 0
abecedario = {chr(letra): 0 for letra in range(ord('a'), ord('z') + 1)}

# Pedimos al usuario que introduzca la frase
frase = input("Introduce una frase: ")

# Convertimos la frase a minúsculas y eliminamos los espacios
frase = frase.lower().replace(" ", "")

# Recorremos cada carácter de la frase
for caracter in frase:
    if caracter in abecedario:  # Solo consideramos las letras
        abecedario[caracter] += 1

# Ordenamos las letras por el número de ocurrencias de mayor a menor
ordenadas = sorted(abecedario.items(), key=lambda item: item[1], reverse=True)

# Filtramos las letras con al menos una ocurrencia
ordenadas = [item for item in ordenadas if item[1] > 0]

# Mostramos las ocurrencias ordenadas
print("Letras ordenadas de mayor a menor ocurrencia:")
for letra, ocurrencias in ordenadas:
    print(f"{letra}: {ocurrencias}")

# Buscamos las letras más y menos repetidas
if ordenadas:
    max_repeticiones = ordenadas[0][1]
    min_repeticiones = ordenadas[-1][1]
    letras_mas_repetidas = [letra for letra, valor in ordenadas if valor == max_repeticiones]
    letras_menos_repetidas = [letra for letra, valor in ordenadas if valor == min_repeticiones]
    
    print("\nLetras más repetidas:", letras_mas_repetidas, "con", max_repeticiones, "repeticiones.")
    print("Letras menos repetidas:", letras_menos_repetidas, "con", min_repeticiones, "repeticiones.")
else:
    print("\nNo se encontraron letras en la frase.")
