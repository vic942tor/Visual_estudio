# Escriba un programa en Python que calcule la suma de los elementos de cada una de las
# diagonales de una matriz.
# Los datos de entrada serán:
# Un número (n) que indica el orden de la matriz (número de filas y columnas que tiene)
# Los n al cuadrado elementos de la matriz.
# Luego se debe mostrar como resultado la suma de los elementos de la diagonal principal y la
# suma de los elementos de la diagonal secundaria.

# Leemos el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz (n): "))  # Tamaño de la matriz (n x n)

# Inicializamos una lista vacía para almacenar la matriz
matriz = []

# Leemos las filas de la matriz
for i in range(n):
    fila = list(map(int, input(f"Ingrese la fila {i+1} (separada por espacios): ").split()))
    matriz.append(fila)

# Imprimimos la matriz
print("\nLa matriz cuadrada que se ha leído:")
for fila in matriz:
    print(" ".join(map(str, fila)))

# Inicializamos las variables para las sumas de las diagonales
suma_principal = 0
suma_secundaria = 0

# Calculamos las sumas de las diagonales
for i in range(n):
    suma_principal += matriz[i][i]  # Elementos de la diagonal principal
    suma_secundaria += matriz[i][n-i-1]  # Elementos de la diagonal secundaria

# Imprimimos los resultados
print(f"\nLa suma de los elementos de la diagonal principal es {suma_principal}")
print(f"La suma de los elementos de la diagonal secundaria es {suma_secundaria}")
