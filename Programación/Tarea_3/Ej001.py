# Dada una lista, extraer todos los elementos cuya frecuencia sea superior a n. Los
# elementos de la lista deben leerse mediante un bucle del cual se sale con la
# secuencia *fin.
# Posteriormente se debe leer el valor de n.

lista = []
#Aquí creamos el bucle para crear la lista y del cual podemos salir exribiendo fin
while True:
    elemento = input("Ingresa un elemento (o 'fin' para terminar): ").lower()
    if elemento == 'fin':
        break
    lista.append(int(elemento))
n = int(input('Inserte un número entero: '))
resultado = []
# Recorremos cada elemento en la lista
for i in range(len(lista)):
    elemento = lista[i]
    # Solo contamos el elemento si no ha sido agregado previamente al resultado
    if elemento not in resultado:
        # Contamos cuántas veces aparece el elemento en la lista
        cuenta = lista.count(elemento)
        if cuenta > n:
            resultado.append(elemento)
print(f'Los números que se repiten más veces que {n} son: {resultado}')



    



