# Un programa que lea un fichero y diga cuantos números hay y cuales son los números

if __name__ == '__main__':
    try:
        fichero = open('./datos_ejemplo01.txt')
    except:
        print('Ha ocurrido un error con la ruta seleccionada, por favor vuelva a introducirla.')
    else:
        total_numero = 0
        lista_numeros = []
        comienza_numeros = False
        numero = ''

        while True:
            caracter = fichero.read(1)
            if caracter:
                if caracter.isdigit():
                    if not comienza_numeros:
                        comienza_numeros = True
                        numero = caracter
                    else:
                        numero += caracter
                else:
                    if comienza_numeros:
                        comienza_numeros = False
                        lista_numeros.append(int(numero))
                        numero = ''
            else:
                if comienza_numeros:
                    lista_numeros.append(int(numero))
                break

        fichero.close()
        print(lista_numeros)
        print(f'En el fichero se han encontrado {len(lista_numeros)} números.')



