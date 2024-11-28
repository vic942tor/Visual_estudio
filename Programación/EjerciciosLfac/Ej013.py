# Escriba un programa en Python que dada una lista de números enteros, el objetivo es encontrar el
# primer elemento no consecutivo entre los elementos de la lista
# Si todos los valores son consecutivos entonces el resultado debe ser None.
# Ejemplos:
# [1, 2, 3, 4, 6, 7, 8] -> 6
# Página 4 de 5
# [101, 102, 103] -> None
# [-5, -4, -3, 0, 3, 4, 5] -> 0
# [1] -> None
# [] -> None
# [-3, -2, -1, 0, 1] -> None 

# Lista de ejemplo
lista = [1, 2, 3, 4, 6, 7, 8]

# Variable para almacenar el primer elemento no consecutivo
resultado = None

# Recorrer la lista para encontrar el primer elemento no consecutivo
for i in range(1, len(lista)):
    if lista[i] != lista[i-1] + 1:
        resultado = lista[i]
        break

# Mostrar el resultado
print(f"El primer elemento no consecutivo es: {resultado}")

