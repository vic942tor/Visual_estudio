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
# Inicializamos el diccionario vacío
diccionario = {}
# Recorremos cada sublista y asignamos al diccionario
for sublista in peliculas:
    clave = sublista[0]  # El primer elemento de la sublista es la clave
    valor = sublista[1:]  # Los demás elementos son el valor asociado
    diccionario[clave] = valor  # Asignamos la clave y el valor en el diccionario
# Mostrar el resultado
print(diccionario)

