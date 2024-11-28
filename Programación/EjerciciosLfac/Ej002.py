# Escriba un programa en Python que dada una lista de números enteros, obtenga otra lista donde
# se eliminen los duplicados. Mantenga el orden de los números en la nueva lista generada.
# Ejemplos de como debe ser la salida del programa debe ser como la que se muestra a
# continuación:
# [2, 3, 2, 2, 1, 5, 4, 2, 4, 9] -> [2, 3, 1, 5, 4, 9]
# [0, 3, 0, 3, 0, 3] -> [0,3]
# [1, 2, 3, 4, 5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5]

# Lista de ejemplo
numeros = [2, 3, 2, 2, 1, 5, 4, 2, 4, 9]

# Lista vacía para almacenar los números sin duplicados
sin_duplicados = []

# Recorremos la lista original
for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print(sin_duplicados)
