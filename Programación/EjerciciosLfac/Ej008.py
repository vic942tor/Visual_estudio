# Escriba un programa en Python que dada una lista de enteros y de string que representan
# números enteros, calcule la suma de todos los valores de la lista como si todos sus elementos
# fueran números. 

# Definir la lista mixta
mi_lista = [1, '2', 3, '4', '5', 6]

# Convertir todos los elementos de la lista a enteros y sumarlos
suma_total = sum(int(x) for x in mi_lista)

# Mostrar el resultado
print(f"La suma total es: {suma_total}")
