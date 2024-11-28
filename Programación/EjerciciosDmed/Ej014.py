# Dado un diccionario de entrada, escriba un programa que lo ordene en base a sus
# valores de forma ascendente.
# Se puede asumir que:
# • Tanto las claves como los valores del diccionario de entrada van a ser cadenas de
# texto.
# • Tanto las claves como los valores del diccionario de entrada no van a contener dos
# puntos ':'
# La salida tendrá que ser una lista de tuplas (clave, valor) ya ordenadas.
# Ejemplos:
# {'a': 'two', 'b': 'one', 'c': ‘three'}
# —> [('b', 'one'), ('c', 'three'), ('a', ‘two')]
# {'mar': 'azul', 'tierra': 'marrón', ‘aire':'blanco'}
# —> [('mar', 'azul'), ('aire', 'blanco'), (‘tierra', ‘marrón')]
#  {'M': 'MacOS', 'L': 'Linux', 'W': ‘Windows'}
# —> [('L', 'Linux'), ('M', 'MacOS'), (‘W', ‘Windows')]
# {'C1': 'Red', 'C2': 'Black', 'C3': 'Red', ‘C4’:'Green'}
# —> [('C2', 'Black'), ('C4', 'Green'), ('C1', ‘Red'), ('C3', ‘Red')]
# { }
# —> [ ] 

# Diccionario de entrada
diccionario = {'a': 'two', 'b': 'one', 'c': 'three'}
# Ordenar el diccionario por valores (de forma ascendente)
ordenado = sorted(diccionario.items(), key=lambda item: item[1])
# Mostrar el resultado
print(ordenado)
