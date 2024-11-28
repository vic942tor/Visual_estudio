# Escriba un programa en Python que dada una lista, genere otra lista eliminando los elementos
# que ocupan posiciones pares.
# Ejemplo: [1, 2, 3, 4, 5, 6] se debe generar la lista [1, 3, 5]

# Lista original
lista = [1, 2, 3, 4, 5, 6]

# Generar la nueva lista eliminando elementos en posiciones pares
lista_filtrada = [lista[i] for i in range(len(lista)) if i % 2 == 0]

# Mostrar el resultado
print(f"La lista filtrada es: {lista_filtrada}")
