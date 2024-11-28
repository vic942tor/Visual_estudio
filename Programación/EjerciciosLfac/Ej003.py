# Escriba un programa en Python que dada una lista que puede tener como elementos números
# enteros y otras listas con números enteros (sólo 1 nivel de anidamiento), se pide que se genere
# una lista aplanada a partir de la original.
# Una lista es aplanada cuando le quitamos el anidamiento de listas que puedan tener. Es decir, se
# quitan los elementos de tipo lista, colocando los elementos que contiene en la lista original en la
# misma posición.
# Un ejemplo es el que se muestra
# [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100,110, 120]] al aplanarla debe quedar así
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120] 

# Lista de ejemplo
numeros = [10, 20, [30, 40, 50], [60, 70], 80, [90, 100, 110, 120]]

# Lista vacía para almacenar los elementos aplanados
aplanada = []

# Recorremos cada elemento de la lista
for item in numeros:
    if isinstance(item, list):
        aplanada.extend(item)  # Si es lista, agregamos sus elementos
    else:
        aplanada.append(item)  # Si no es lista, agregamos el elemento directamente

print(aplanada)
