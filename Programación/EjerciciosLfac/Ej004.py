# Escribir un programa en Python que dada una lista de elementos, genere otra lista eliminando los
# elementos duplicados consecutivos.
# Ejemplos:
# La lista [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4] debe dar como resultado la lista [0, 1, 2, 3, 4, 5,
# 6, 7, 8, 9, 4] y con la lista ['a', 'b', 'b', 'b', 'c', ‘b’] debe dar ['a', 'b', 'c', 'b']

# Lista de ejemplo
lista = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# Lista vacía para la nueva lista sin duplicados consecutivos
lista_sin_duplicados = []

# Recorremos la lista original
for i in range(len(lista)):
    if i == 0 or lista[i] != lista[i - 1]:
        lista_sin_duplicados.append(lista[i])

print(lista_sin_duplicados)
