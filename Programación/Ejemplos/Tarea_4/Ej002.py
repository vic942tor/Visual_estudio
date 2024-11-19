# Escribir un programa en Python que permita encontrar la/las claves que tengan el
# máximo valor. El resultado se debe mostrar como una tupla, en la que el primer
# elemento es/son las claves en la que se consigue el máximo y el segundo
# elemento de la tupla es el máximo valor encontrado.

d1 = {9: '11', 15: '2', 100: '3', 90: '15', 60: '44', 23: '49'}
#Buscamos el valor máximo en los valores del diccionario
max_valor = max(d1.values())
#Aquí buscamos las claves asociadas a ese valor máximo
claves_maximas = []
for clave, valor in d1.items():
    if valor == max_valor:
        claves_maximas.append(clave)
#Crear el resultado como una tupla
resultado = (claves_maximas, max_valor)
print(resultado)


    
    