# Escribir un programa que lea un string en pantalla que represente la dirección de
# un correo electrónico y diga si es válida o no. Lo que se pide es que se revise el
# formato.
# Una dirección de correo debe tener el siguiente formato:
# aaaaaaaaaaaaaaaa@aaaaaaaaa.aaaa
# Es decir, antes del arroba debe existir al menos dos caracteres y un máximo de 16
# y no debe empezar por número, a continuación el carácter ‘@‘, seguido de
# cualquier número de caracteres o dígitos, (que no comienza por dígito), para
# finalizar debe estar el ‘.’ seguido de al menos 2 y hasta 4 caracteres, ninguno de
# los cuales puede ser un dígito.
correo = input("Establece una dirección de correo para verificar si es valida: ")
if '.' in correo and '@' in correo:
    # Separamos la dirección de correo en dos partes, antes y después del @.
    comprobacion = correo.split('@')
    #Aquí estamos separando la parte que tiene delante el @ para realizar las comprobaciones, lo separo mediante el .
    comprobacion2 = comprobacion[1].split('.')
    if len(comprobacion[0]) < 2 or len(comprobacion[0]) > 16:
        print("La dirección de correo no es válida.")
    elif correo[0].isdigit():
        print("La dirección de correo no es válida.")
    elif comprobacion[1][0].isdigit():
        print("La dirección de correo no es válida.")
    elif len(comprobacion2[1]) < 2 or len(comprobacion2[1]) > 4:
        print("La dirección de correo no es válida.")
    else:
        print("La dirección de correo es válida.")
else:
    print("La dirección de correo no es válida")
