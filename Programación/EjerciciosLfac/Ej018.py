# Ejercicio 03: Modificar el programa anterior para los datos de las listas se ingresen por
# teclado.

# Solicitar al usuario el tamaño de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Crear la matriz vacía
matriz = []

# Solicitar los elementos de la matriz
print("Ingrese los elementos de la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento en la posición [{i+1}, {j+1}]: "))
        fila.append(elemento)
    matriz.append(fila)

# Calcular la suma de cada fila
print("\nSuma de los elementos por filas:")
for fila in matriz:
    suma_fila = sum(fila)  # Calcular la suma de la fila
    print(suma_fila)

# Calcular la suma de cada columna
print("\nSuma de los elementos por columnas:")
for j in range(columnas):
    suma_columna = 0
    for i in range(filas):  # Recorrer cada fila para sumar los elementos de la columna
        suma_columna += matriz[i][j]
    print(suma_columna)
