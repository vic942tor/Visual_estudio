#Escriba un programa que dada una frase que se introduce por tecladoretorneundiccionario asociando a cada letra 
# la cantidad de veces que aparece en la misma. Cadavalordeldiccionario debe considerar tanto las apariciones en 
# mayúscula como en minúsculadelaletracorrespondiente. Los espacios deben ser ignorados. Para esta primera versión 
# usar undiccionarioen la que cada elemento será como sigue:
# {letra: valor}
# letra: será cada una de las letras del abecedario
# valor: será el número de ocurrencias de esa letra en el texto.
# Inicialmente el diccionario tiene todas las letras creadas con 
#  valor 0. Después se actualiza leyendo la frase los campos valor 
# de las letras que ésta contenga. Posteriormente se debe indicar: 
#  la(s) letra(s) que está(n) repetidas más veces.  la(s) letra(s) que 
# está(n) repetidas menos veces.  Las letras del abecedario que no están 
# la frase.

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

# Filtramos las letras no usadas
letras_no_usadas = [letra for letra, valor in abecedario.items() if valor == 0]

# Buscamos las letras más repetidas
max_repeticiones = max(abecedario.values())
letras_mas_repetidas = [letra for letra, valor in abecedario.items() if valor == max_repeticiones]

# Buscamos las letras menos repetidas (pero usadas al menos una vez)
min_repeticiones = min(valor for valor in abecedario.values() if valor > 0)
letras_menos_repetidas = [letra for letra, valor in abecedario.items() if valor == min_repeticiones]

# Mostramos los resultados
print("Letras más repetidas:", letras_mas_repetidas, "con", max_repeticiones, "repeticiones.")
print("Letras menos repetidas:", letras_menos_repetidas, "con", min_repeticiones, "repeticiones.")
print("Letras no usadas:", letras_no_usadas)
