# Escriba un programa en Python para comprobar si la lista contiene tres números
# comunes consecutivos.
# Inicializamos una lista vacía para almacenar los elementos ingresados
lista = []
while True:
    elemento = input("Ingresa un elemento (o 'fin' para terminar): ").strip().lower()
    if elemento == 'fin':
        break
    try:
        # Convertimos el elemento a entero y lo añadimos a la lista
        lista.append(int(elemento))
    except:
        print("Por favor, ingresa un número válido o 'fin' para terminar.")
resultado = []
# Recorremos la lista hasta el tercer último elemento
for i in range(len(lista) - 2):
    # Verificamos si el elemento actual y los dos siguientes son iguales
    if lista[i] == lista[i + 1] == lista[i + 2]:
        # Añadimos el número al resultado si no está ya incluido
        if lista[i] not in resultado:
            resultado.append(lista[i])
if resultado:
    print("Los números que se repiten tres veces consecutivas son:", resultado)
else:
    print("No hay números que se repitan tres veces consecutivas.")

