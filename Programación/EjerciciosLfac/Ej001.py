# Escriba un programa en Python que dada una lista de valores numéricos enteros obtenga su
# máximo valor. En este ejercicio no se puede usar los métodos max() y sorted().
# Ejemplos:
# La salida debe mostrarse como se muestra a continuación.
# [ 3, 7, 100, 2, -20] -> 100
# [200, -100, 4, 8, 200] -> 200
# [-7, -10, -6, -3] -> -3

# Lista de ejemplo
numeros = [3, 7, 100, 2, -20]

# Inicializamos el valor máximo con un número muy bajo
maximo = numeros[0]

# Recorremos la lista para encontrar el máximo
for num in numeros:
    if num > maximo:
        maximo = num

print(maximo)
