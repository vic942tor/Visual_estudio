# Ejercicio 08: Escriba una programa que tome dos listas A de caracteres y B de números, devuelvauna diccionario 
# con todos las parejas ordenadas con primera componente en A (la clave) ysegundaen B (el valor). La lista puede tener 
# elementos repetidos, téngalo en cuenta a la horadecreareldiccionario.

# Entrada de las listas A y B
A = input("Introduce la lista de caracteres (separados por espacios): ").split()
B = input("Introduce la lista de números (separados por espacios): ").split()

# Convertimos los elementos de B a enteros
B = [int(num) for num in B]

# Crear el diccionario
diccionario = {}

# Generar las combinaciones
for char in A:
    for num in B:
        if char in diccionario:
            diccionario[char].append(num)
        else:
            diccionario[char] = [num]

# Mostrar el diccionario resultante
print("Diccionario generado:")
for clave, valores in diccionario.items():
    print(f"{clave}: {valores}")
