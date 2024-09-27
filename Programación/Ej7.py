#Crear una "forma de enciptado"
ALFBETO = "abcdefghijklmnñopqrstuvwxyz"
operacion = input("Quieres cifrar (C) o descifrar (D) un texto:  ").upper
clave = int(input("Introduce la clave:  "))
mensaje = input("Introduce el mensaje:  ")
if operacion == "C":
    iteracion = 0
    while iteracion < len(mensaje):
        posicion = ALFBETO.find(mensaje[iteracion])
        nva_posicion = posicion + clave
        mje_cifrado =+ ALFBETO[nva_posicion]
        pass
elif operacion == "D":
    pass
else:
    print("Error opción incorrecta, Vuelve a introducir el texto de nuevo.")