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

def puedecomer(pieza1, pieza2):
    # Comparamos las figuras de las piezas
    if pieza1[0] != pieza2[0]:
        return False
    
    # Obtenemos las posiciones de las piezas
    
