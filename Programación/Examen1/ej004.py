# Se quiere escribir un programa en Python que pida una frase al usuario y que
# compruebe si esta contiene todas las letras del alfabeto español. 
# Las letras del alfabeto español son las siguientes:
# abcdefghijklmnñopqrstuvwxyz
# Se debe tener en cuenta que además de las letras minúsculas están las
# correspondientes mayúsculas.
ALFABETO = 'abcdefghijklmnñopqrstuvwxyz'
ACENTOS = 'áéíóú'
ACENTOS[0] == ALFABETO[0]
ACENTOS[1] == ALFABETO[4]
ACENTOS[2] == ALFABETO[8]
ACENTOS[3] == ALFABETO[15]
ACENTOS[4] == ALFABETO[21]
frase = input('escriba una frase para saber si tiene todas las letras del alfabeto español: ').lower()
for i in ALFABETO:
    if i not in frase:
        print('no contiene todas las letras del alfabeto')
        break
else:
    print('contiene todas las letras del alfabeto')
