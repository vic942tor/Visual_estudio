# Crear una "forma de cifrado" tipo César
ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
ALFABETO_INVERTIDO = ALFABETO[::-1]
OPERACION_CIFRAR = "C"
OPERACION_DESCIFRAR = "D"

# Solicitar al usuario la operación, clave y mensaje
operacion = input("¿Quieres cifrar (C) o descifrar (D) un texto? ").upper()
mensaje = input("Introduce el mensaje: ").lower()

mje_resultado = ""

if operacion == OPERACION_CIFRAR:
    iteracion = 0
    while iteracion < len(mensaje):
        caracter = mensaje[iteracion]
        posicion = ALFABETO.find(caracter)
        if posicion != -1:
            mje_resultado += ALFABETO_INVERTIDO[posicion]
        else:
            # Si el carácter no está en el alfabeto, se agrega sin cambios
            mje_resultado += caracter
        iteracion += 1
    print("Mensaje cifrado:", mje_resultado)

elif operacion == OPERACION_DESCIFRAR:
    iteracion = 0
    while iteracion < len(mensaje):
        caracter = mensaje[iteracion]
        posicion = ALFABETO_INVERTIDO.find(caracter)
        if posicion != -1:
            mje_resultado += ALFABETO[posicion]
        else:
            # Si el carácter no está en el alfabeto, se agrega sin cambios
            mje_resultado += caracter
        iteracion += 1
    print("Mensaje descifrado:", mje_resultado)

else:
    print("Error: opción incorrecta, por favor elige 'C' para cifrar o 'D' para descifrar.")