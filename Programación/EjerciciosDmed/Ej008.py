# Dado un diccionario escriba un programa en Python que compruebe si todos sus
# valores son iguales o no.
# Ejemplos:
# {'a': 1, 'b': 1, 'c': 1, 'd': 1} El valor a devolver es True
# {'a': 1, 'b': 2, 'c': 3, 'd': 4} El valor a devolver es False
# {1: 'a', 2: 'b', 3: 'c', 4: ‘d'} El valor a devolver es False
# {1: 'a', 2: 'a', 3: 'a', 4: ‘a'} El valor a devolver es True
# {} El valor a devolver es True 

# Ejemplo de diccionario
diccionario1 = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
diccionario2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
diccionario3 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
diccionario4 = {1: 'a', 2: 'a', 3: 'a', 4: 'a'}
diccionario5 = {}

# Diccionario a comprobar
diccionario = diccionario2  # Puedes cambiar este valor para probar diferentes diccionarios

# Comprobar si el diccionario está vacío
if not diccionario:
    print(True)
else:
    # Obtener los valores del diccionario
    valores = list(diccionario.values())

    # Comprobar si todos los valores son iguales
    if len(set(valores)) == 1:
        print(True)
    else:
        print(False)
