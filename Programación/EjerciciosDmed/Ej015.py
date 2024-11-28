# Un cliente compra un artículo en una tienda con dinero suficiente (mayor o igual) que
# el importe del artículo. Por lo tanto hay que devolver el cambio. La tienda dispone de
# una serie concreta de monedas/billetes para dar la vuelta. El objetivo del ejercicio es
# devolver el cambio al cliente empezando por la moneda/billete más grande y llegando
# hasta la más pequeña. El cambio se debe devolver en un diccionario de nombre
# la_vuelta. Suponemos que tenemos una variable importe_a_devolver con el importe
# que se debe devolver al cliente y una lista de nombre cambio con los billetes y
# moneda que dispone la tienda.
# Notas:
# • Si el dinero es justo hay que devolver un diccionario vacío.
# • Si el cambio no es posible hay que devolver None
# Ejemplos:
# importe_a_devolver = 20
# cambio = [5, 2, 1]
# El resultado debe ser: la_vuelta = {5: 4}
# importe_a_devolver = 7
# cambio = [2, 1, 0.5]
# El resultado debe ser: la_vuelta = {2: 3, 1: 1}
# importe_a_devolver = 13.5
# cambio = [5, 2, 0.5]
# El resultado debe ser: la_vuelta = {5: 2, 2: 1, 0.5: 3}
# importe_a_devolver = 11
# cambio = [0.1, 0.5, 2]
# El resultado debe ser: la_vuelta = {2: 5, 0.5: 2.0}
# importe_a_devolver = 0
# cambio = [0.5, 0.2, 0.1]
# El resultado debe ser: la_vuelta = { }
# importe_a_devolver = 4.75
# cambio = [1, 5, 0.2]
# El resultado debe ser: la_vuelta = None

# Variables de entrada
importe_a_devolver = 20
cambio = [5, 2, 1]
# Ordenar las monedas y billetes de mayor a menor
cambio.sort(reverse=True)
# Inicializar el diccionario que devolverá el cambio
la_vuelta = {}
# Comprobar si el importe es 0, en ese caso no se necesita cambio
if importe_a_devolver == 0:
    la_vuelta = {}
# Si el importe es negativo o no es posible devolver el cambio
elif importe_a_devolver < 0:
    la_vuelta = None
else:
    for moneda in cambio:
        # Calcular cuántas veces se puede usar la moneda actual
        cantidad = int(importe_a_devolver // moneda)
        
        # Si la cantidad es mayor que 0, se añade al diccionario
        if cantidad > 0:
            la_vuelta[moneda] = cantidad
            # Reducir el importe a devolver por el valor de la moneda * cantidad
            importe_a_devolver -= cantidad * moneda    
        # Si ya no queda importe por devolver, salir del bucle
        if importe_a_devolver == 0:
            break

    # Si después de todas las operaciones sigue habiendo importe, es que no se puede devolver
    if importe_a_devolver > 0:
        la_vuelta = None
# Resultados de ejemplo:
print(la_vuelta)  # Resultado esperado: {5: 4}
