# Dado un historial de compras de clientes representado como un diccionario:
# compras = {
#  'Juan': ['manzanas', 'plátanos', 'café'],
#  'Ana': ['café', 'leche', 'pan'],
#  'Luis': ['manzanas', 'café', 'pan']
# }
# Pregunta 01: (1,0 puntos)
# Escribe un programa en Python que genere una lista de nombre
# producto_todos en la que aparecen los productos que han sido comprado
# por todo los clientes.
# Pregunta 02: (2,0 pts)
# Escribe un programa en Python que genere un diccionario de nombre
# clientes_exlusivos en la que se guardará los clientes que tienen productos en
# exclusividad. En exclusividad significa que sólo lo vende ese cliente.
# La clave del diccionario es el nombre del cliente
# El valor una lista de productos que vende en exclusividad.

compras = {
 'Juan': ['manzanas', 'plátanos', 'café'],
 'Ana': ['café', 'leche', 'pan'],
 'Luis': ['manzanas', 'café', 'pan']
}
#Aquí estamos comprobando los productos repetidos en todos los clientes seleccionando la lista mediante la Key del diccionario
compra_comun = set(compras[list(compras.keys())[0]])
for compras1 in compras.values():
        compra_comun &= set(compras1)  
print(f'El producto comprado por todos es: {compra_comun}')
#Creamos un set con todos los productos comprados por cada persona
productos_comprados = {persona: set(productos) for persona, productos in compras.items()}
# Calcular los productos exclusivos de cada comprador
for comprador, productos_general in productos_comprados.items():
    productos_exclusivos = productos_general.copy()  
    for otro_comprador, productos in productos_comprados.items():
        if comprador != otro_comprador:
            productos_exclusivos -= productos 
    print(f'Producto exclusivo de {comprador}: {productos_exclusivos}')





