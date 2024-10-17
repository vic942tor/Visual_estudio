#Separar con partition
texto = "123:45:6"
texto_aux = texto[:]
while True:
    tupla_dev = (texto.partition(":"))
    if tupla_dev[2] != "":
        print(tupla_dev[0])
        texto = tupla_dev[2]
    else:
        print(tupla_dev[0])
        break
