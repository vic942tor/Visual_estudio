def validar_entrada(ficha):
    """
    Valida la entrada de una ficha del ajedrez.

    """
    figuras_validas = {"peón", "torre", "caballo", "alfil", "reina", "rey"}
    filas_validas = set(range(1, 9))
    columnas_validas = {"A", "B", "C", "D", "E", "F", "G", "H"}

    if not isinstance(ficha, tuple) or len(ficha) != 2:
        return False

    figura, posicion = ficha
    if figura not in figuras_validas:
        return False

    if not isinstance(posicion, tuple) or len(posicion) != 2:
        return False

    fila, columna = posicion
    if fila not in filas_validas or columna not in columnas_validas:
        return False

    return True

def convertir_posicion_a_coordenadas(posicion):
    """
    Convierte la posición del tablero de ajedrez (fila, columna) en coordenadas numéricas.

    Args:
        posicion (tuple): Tupla con formato (fila, columna).

    Returns:
        tuple: Coordenadas numéricas (fila, columna).
    """
    fila, columna = posicion
    columna_num = ord(columna.upper()) - ord('A') + 1
    return (fila, columna_num)

def puedecomer(pieza1, pieza2):
    """
    Determina si la pieza1 puede comer a la pieza2.

    """
    if not (validar_entrada(pieza1) and validar_entrada(pieza2)):
        raise ValueError("Entrada inválida para una o ambas piezas.")

    figura1, posicion1 = pieza1
    _, posicion2 = pieza2

    fila1, col1 = convertir_posicion_a_coordenadas(posicion1)
    fila2, col2 = convertir_posicion_a_coordenadas(posicion2)

    if figura1 == "peón":
        if fila1 + 1 == fila2 and abs(col1 - col2) == 1:
            return True

    elif figura1 == "torre":
        if fila1 == fila2 or col1 == col2:
            return True

    elif figura1 == "caballo":
        if (abs(fila1 - fila2), abs(col1 - col2)) in [(2, 1), (1, 2)]:
            return True

    elif figura1 == "alfil":
        if abs(fila1 - fila2) == abs(col1 - col2):
            return True

    elif figura1 == "reina":
        if fila1 == fila2 or col1 == col2 or abs(fila1 - fila2) == abs(col1 - col2):
            return True

    elif figura1 == "rey":
        if max(abs(fila1 - fila2), abs(col1 - col2)) == 1:
            return True

    return False

def main():
    while True:
        try:
            pieza1 = input("Ingrese la primera pieza (formato: figura, fila, columna): ")
            figura1, fila1, columna1 = pieza1.split(",")
            pieza1 = (figura1.strip().lower(), (int(fila1.strip()), columna1.strip().upper()))

            pieza2 = input("Ingrese la segunda pieza (formato: figura, fila, columna): ")
            figura2, fila2, columna2 = pieza2.split(",")
            pieza2 = (figura2.strip().lower(), (int(fila2.strip()), columna2.strip().upper()))

            resultado = puedecomer(pieza1, pieza2)
            print(f"La pieza {pieza1} puede comer a la pieza {pieza2}: {resultado}")

        except ValueError as e:
            print(f"Error en la entrada: {e}")

        continuar = input("\u00bfDesea probar con otras piezas? (si/no): ").strip().lower()
        if continuar == "no":
            break

if __name__ == "__main__":
    main()
