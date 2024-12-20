# Dada una lista, extraer todos los elementos cuya frecuencia sea superior a n. Los
# elementos de la lista deben leerse mediante un bucle del cual se sale con la
# secuencia *fin.
# Posteriormente se debe leer el valor de n.


lista = []
while True:
    elemento = input("Ingresa un elemento (o 'fin' para terminar): ").strip().lower()
    if elemento == 'fin':
        break
    try:
        lista.append(int(elemento))
    except:
        print("Por favor, ingresa un número válido o 'fin' para terminar.")
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
if resultado:
    print(f'Los números que se repiten más veces que {n} son: {resultado}')
else:
    print('No hay números que se repiten más veces que', n)



    



