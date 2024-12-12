# La idea es realizar un programa en Python que defina la función
# puedecomer( pieza1, pieza2 ) y que retorna un valor booleano. Este valor
# retornado será True si la pieza1 puede comer a la pieza2 y False en caso contrario.
# Definimos los parámetros de la siguiente forma.
# pieza1 y pieza2 son tuplas que tienen el siguiente formato: ( figura, posición )
# Donde
# • figura: es un string que indica una pieza del ajedrez. Los valores que puede
# tomar son los siguientes: peón, torre, caballo, alfil, reina y rey
# • posición: es una tupla con dos elementos que indican la posición de la pieza en
# el tablero de ajedrez ( fila, columna ) donde
# • fila es un valor entre 1 y 8
# • columna una letra entre A y H

def validacion_piezas(pieza):
    """Valida que la entrada tenga el formato correcto."""
    try:
        figura, fila, columna = pieza.split(",")
        figura = figura.strip().lower()
        fila = int(fila.strip())
        columna = columna.strip().upper()

        if figura not in ["peón", "torre", "caballo", "alfil", "reina", "rey"]:
            return False
        if not (1 <= fila <= 8):
            return False
        if columna not in "ABCDEFGH":
            return False
        return True
    except ValueError:
        return False
def principal():
    while True:
        piezablanca = input('Introduce la pieza y la posición el el siguiente formato (pieza, fila, columna): ')
        piezanegra = input('Introduce la pieza y la posición de la otra pieza en el siguiente formato (pieza, fila, columna): ')
        if not validacion_piezas(piezablanca) or not validacion_piezas(piezanegra):
            print('Formato de pieza incorrecto. Intente de nuevo.')
            continue
        piezablanca1, filablanca1, columnablanca1 = piezablanca.split(',')
        piezablanca = (piezablanca1.strip().lower(), int(filablanca1.strip()), columnablanca1.strip().upper())
        piezanegra1, filanegra1, columnanegra1 = piezanegra.split(',')
        piezanegra = (piezanegra1.strip().lower(), int(filanegra1.strip()), columnanegra1.strip().upper())
        print(piezanegra)
        print(piezablanca)

if __name__ == "__main__":
    principal()