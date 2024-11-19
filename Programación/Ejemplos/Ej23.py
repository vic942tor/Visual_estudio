#Escribe un prgrama en Python que mediante un diccionario cuente el número de veces que aparece una letra en una frase leída
#Una vez creado el diccionario se debe recorrer para mostrar por línea el número de ocurrencias de cada letra


# frase = input("Introduce una frase: ").lower()
# diccionario = {}
# for letra in frase:
#     if letra not in diccionario:
#         diccionario[letra] = 1
#     else:
#         diccionario[letra] += 1
# print (diccionario)

frase = input("Introduce una frase: ").lower()
diccionario = {}
for letra in frase:
    diccionario.setdefault(letra,0)
    diccionario[letra] += 1
print('Las letras repetidas son las siguientes:')
for letra in diccionario:
    print(f"{letra}: {diccionario[letra]}")