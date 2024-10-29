# En este ejercicio se quiere realizar un programa de Python que implemente la
# variante del Código de César que se describe a continuación:
# Para este algoritmo de cifrado se necesita una clave numérica cuyo valor debe ser
# menor o igual que un tercio de la longitud del mensaje a encriptar y tener un valor
# que sea mayor a 3. Esto garantiza que el cifrado obtenido no sea tan fácil de
# descifrar...

mensaje = input('Escriba un mensaje para encriptarlo: ')
# Calcular la clave como un tercio de la longitud del mensaje
clave = len(mensaje) // 3
# Validar la clave
if clave <= 3:
    print("Error: La clave debe ser mayor a 3.")
else:
    encriptado = ""
    longitud_mensaje = len(mensaje)
    #Aquí dividimos el mensaje en bloques y leer por columnas
    for i in range(clave):
        for j in range(i, longitud_mensaje, clave):
            encriptado += mensaje[j]
    print("Mensaje encriptado:", encriptado)

