# Un programa que lea un fichero y diga cuantos números hay y cuales son los números

if __name__ == '__main__':
    try:
        fichero = open(input('Introduzca la ruta del fichero que quiera comprobar: '))
    except Exception as e:
        print('Ha ocurrido un error con la ruta seleccionada, por favor vuelva a introducirla.')
        lista_numeros = []  # Asegurar que la variable esté definida
    else:
        total_numero = 0
        lista_numeros = []
        comienza_numeros = False
        numero = ''  # Inicializar la variable fuera del bucle

        while True:
            caracter = fichero.read(1)
            if caracter:  # Mientras el carácter no sea vacío
                if caracter.isdigit():  # Es dígito
                    if not comienza_numeros:
                        comienza_numeros = True
                        numero = caracter
                    else:
                        numero += caracter
                else:  # No es dígito
                    if comienza_numeros:
                        comienza_numeros = False
                        lista_numeros.append(int(numero))  # Agregar el número como entero
                        numero = ''
            else:  # Fin del archivo
                if comienza_numeros:  # Añadir el último número si es necesario
                    lista_numeros.append(int(numero))
                break

        fichero.close()

    print(lista_numeros)
    print(f'En el fichero se han encontrado {len(lista_numeros)} números.')



