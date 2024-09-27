#bucle de lectura de números positivos
while True:
    valor = input("Escribe un número positivo:  ")
    try:
        numero = float(valor)
    except:
        print("Establece un número")
    else:
        if numero >= 0:
            print(f"Número leido: {numero}")
        else:
            print("Fin de ejecución")
            break