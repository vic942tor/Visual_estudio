# Escriba un programa en Python que dada una lista de números enteros positivos y un número no
# negativo N, calcule el valor del elemento en la posición N elevado a N.
# Ejemplo: [10, 20, 30, 40, 50] y N = 4 el resultado es 6250000 

# Lista de números
lista = [10, 20, 30, 40, 50]

# Pedir el número N
N = int(input("Introduce el valor de N: "))

# Verificar si N es una posición válida en la lista
if N < len(lista) and N >= 0:
    # Calcular el valor del elemento en la posición N elevado a N
    resultado = lista[N] ** N
    print(f"El resultado de elevar el elemento en la posición {N} a {N} es: {resultado}")
else:
    print("El valor de N no es válido.")
