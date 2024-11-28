# Dada una lista de valores numéricos enteros, obtenga el resultado de multiplicar todos los valores
# en orden.
# Ejemplos:
# [1, 2, 3, 4] -> 24
# [7, 13, 2, -1] -> -182
# [1] -> 1
# [] -> 0

# Lista de ejemplo
lista = [1, 2, 3, 4]

# Inicializar la variable para el producto
producto = 1

# Si la lista no está vacía, multiplicar los elementos
if len(lista) > 0:
    for numero in lista:
        producto *= numero
else:
    producto = 0

# Mostrar el resultado
print(f"El producto de todos los valores es: {producto}")
