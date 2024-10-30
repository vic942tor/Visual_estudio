# Se quiere escribir un programa en Python que pida una frase al usuario y que
# compruebe si esta contiene todas las letras del alfabeto español. 
# Las letras del alfabeto español son las siguientes:
# abcdefghijklmnñopqrstuvwxyz
# Se debe tener en cuenta que además de las letras minúsculas están las
# correspondientes mayúsculas.

ALFABETO = 'abcdefghijklmnñopqrstuvwxyz'
ACENTOS = 'áéíóú'
#Aquí estamos diciendole al programa la equivalencia de los acentos a las vocales normales de alfabeto
frase = input('escriba una frase para saber si tiene todas las letras del alfabeto español: ').lower()
frase = frase.replace('á','a')
frase = frase.replace('é','e')
frase = frase.replace('í','i')
frase = frase.replace('ó','o')
frase = frase.replace('ú','u')
for i in ALFABETO:
    if i not in frase:
        print('No contiene todas las letras del alfabeto')
        break
else:
    print('contiene todas las letras del alfabeto')
