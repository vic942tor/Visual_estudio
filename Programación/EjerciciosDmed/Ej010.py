# Dado un diccionario cuyos valores son listas, genere un diccionario nuevo donde se
# borre el contenido de dichas listas.
# Resuelva el ejercicio utilizando diccionarios por comprensión. 

# Diccionario de ejemplo
diccionario = {
    'a': [1, 2, 3],
    'b': [4, 5],
    'c': [6, 7, 8, 9]
}

# Crear un nuevo diccionario con listas vacías como valores
nuevo_diccionario = {clave: [] for clave in diccionario}

# Mostrar el resultado
print(nuevo_diccionario)
