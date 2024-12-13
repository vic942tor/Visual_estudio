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

def puedecomer(pieza1, pieza2, color="blancas"):
    """
    Verifica si pieza1 puede comer a la pieza2.
    color indica el movimiento del peón ('blancas' o 'negras').
    """
    figura1, (fila1, columna1) = pieza1
    figura2, (fila2, columna2) = pieza2
    columnas = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
# Convertir las columnas de letras a números usando el diccionario
    columna1 = columnas[columna1]
    columna2 = columnas[columna2]
    if figura1 == "peón":
# El peón solo puede comer una casilla en diagonal y hacia adelante
        if color == "blancas":
            if fila1 == fila2 + 1 and abs(columna1 - columna2) == 1:
                return True
        elif color == "negras":
            if fila1 == fila2 - 1 and abs(columna1 - columna2) == 1:
                return True
        return False
    elif figura1 == "torre":
# La torre se mueve y captura en línea recta (vertical u horizontal)
        if fila1 == fila2 or columna1 == columna2:
            return True
        return False
    elif figura1 == "caballo":
# El caballo se mueve en "L" (dos casillas en una dirección y una en la perpendicular)
        if (abs(fila1 - fila2) == 2 and abs(columna1 - columna2) == 1) or \
           (abs(fila1 - fila2) == 1 and abs(columna1 - columna2) == 2):
            return True
        return False
    elif figura1 == "alfil":
# El alfil se mueve en diagonal (igual cantidad de casillas en ambas direcciones)
        if abs(fila1 - fila2) == abs(columna1 - columna2):
            return True
        return False
    elif figura1 == "reina":
# La reina se mueve en línea recta o en diagonal
        if fila1 == fila2 or columna1 == columna2 or abs(fila1 - fila2) == abs(columna1 - columna2):
            return True
        return False
    elif figura1 == "rey":
# El rey se mueve una casilla en cualquier dirección
        if abs(fila1 - fila2) <= 1 and abs(columna1 - columna2) <= 1:
            return True
        return False
    return False
def principal():
    while True:
        piezablanca = input('Introduce la pieza y la posición en el siguiente formato (pieza, fila, columna): ')
        piezanegra = input('Introduce la pieza y la posición de la otra pieza en el siguiente formato (pieza, fila, columna): ')
        if not validacion_piezas(piezablanca) or not validacion_piezas(piezanegra):
            print('Formato de pieza incorrecto. Intente de nuevo.')
            continue
        piezablanca = piezablanca.split(',')
        pieza1 = (piezablanca[0].strip().lower(), (int(piezablanca[1].strip()), piezablanca[2].strip().upper()))
        piezanegra = piezanegra.split(',')
        pieza2 = (piezanegra[0].strip().lower(), (int(piezanegra[1].strip()), piezanegra[2].strip().upper()))
        color = input("Indica el color de las blancas (blancas/negras): ").strip().lower()
        if color not in ["blancas", "negras"]:
            print("Color inválido. Usando 'blancas' por defecto.")
            color = "blancas"
        if puedecomer(pieza1, pieza2, color):
            print(f"La pieza {pieza1[0]} en {pieza1[1]} puede capturar a la pieza {pieza2[0]} en {pieza2[1]}.")
        else:
            print(f"La pieza {pieza1[0]} en {pieza1[1]} no puede capturar a la pieza {pieza2[0]} en {pieza2[1]}.")
        continuar = input("¿Quieres probar con otras piezas? (sí/no): ").strip().lower()
        if continuar == "no":
            break
if __name__ == "__main__":
    principal()


