# Escriba un programa en Python que dada una lista de listas con varios elementos,
# obtenga un diccionario donde las claves serán los primeros elementos de las sublistas
# y el valor será una lista con los restantes elementos de las subsistas.
# Ejemplo:
# [['Episode IV - A New Hope', 'May 25', 1977, 'George Lucas'], ['Episode V - The Empire
# Strikes Back', 'May 21', 1980], ['Episode VI - Return of the Jedi', 'May 25', 1983]]
# El resultado debe ser
# {'Episode IV - A New Hope': ['May 25', 1977, 'George Lucas'], 'Episode V - The Empire
# Strikes Back': ['May 21', 1980], 'Episode VI - Return of the Jedi': ['May 25', 1983]}

# Lista de listas
peliculas = [
    ['Episode IV - A New Hope', 'May 25', 1977, 'George Lucas'],
    ['Episode V - The Empire Strikes Back', 'May 21', 1980],
    ['Episode VI - Return of the Jedi', 'May 25', 1983]
]

# Crear el diccionario
diccionario = {sublista[0]: sublista[1:] for sublista in peliculas}

# Mostrar el resultado
print(diccionario)
