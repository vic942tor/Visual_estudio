# Escriba un programa en Python que pida al usuario una frase y muestre los
# números y la cantidad total de números que aparecen en la cadena leída desde el
# teclado.
# Con número no queremos decir dígito entre letras , sino número propiamente
# dicho, es decir, secuencia de dígitos separados del resto de caracteres por medio
# del espacio en blanco.
# Solicitar al usuario que introduzca una frase

frase = input("Introduce una frase y el programa dirá cuántos números hay: ").split(" ")
numeros_encontrados = []
#Aquí vamos mirando por cada parte del split a ver si se cumple la condición de ser un número y si es un número, lo añadimos a la lista de numeros_encontrados
for i in frase:
    if i.isdigit():
        numeros_encontrados.append(i)
#Mostrar los números encontrados y la cantidad total
if numeros_encontrados:
    print("Números encontrados en la cadena:")
    for numero in numeros_encontrados:
        print(numero, end=" ")
    print(f"\nCantidad total de números encontrados: {len(numeros_encontrados)}")
else:
    print("Números encontrados en la cadena: \nNinguno")
    print("En total se han encontrados 0 números en la cadena")