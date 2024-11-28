# Dados dos diccionarios de entrada, escriba un programa en Python que mezcle ambos
# diccionarios en uno único de salida, sin usar métodos de mezcla definidos en Python
# como: a.update(b)
# Ejemplos:
# dict_a = {'a': 1, 'b': 2}
# dict_b = {'a': 3, 'c': 4}
# dict_c = {'a': 3, 'b': 2, 'c': 4}
# dict_a = {0: 1, 1: 0}
# dict_b = {0: 0, 1: 1}
# dict_c = {0: 0, 1: 1}
# dict_a = {}
# dict_b = {'x': 2.1, 'y': 3.4}
# dict_c = {'x': 2.1, 'y': 3.4}
# dict_a = {}
# dict_b ={}
# dict_c = {} 

# Diccionarios de entrada
dict_a = {'a': 1, 'b': 2}
dict_b = {'a': 3, 'c': 4}
# Diccionario de salida
dict_c = {}
# Añadir elementos de dict_a al dict_c
for clave, valor in dict_a.items():
    dict_c[clave] = valor
# Añadir elementos de dict_b al dict_c
for clave, valor in dict_b.items():
    dict_c[clave] = valor
# Mostrar el diccionario resultante
print(dict_c)
