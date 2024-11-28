# Usted es encargado de una empresa de merchandising y dispone de un cierto stock
# para los artículos. El cliente hace un pedido especificando el artículo y la cantidad
# requerida. Usted debe comprobar si existe stock para la cantidad solicitada del
# artículo indicando True o False.
# Ejemplos:
# {'pen': 20, 'cup': 11, 'keyring': 40}
# Compra: ‘cup’
# Cantidad pedida: 9 -> debe devolver True
# {'pen': 20, 'cup': 11, 'keyring': 40}
# Compra: ‘pen’
# Cantidad pedida: 21 -> debe devolver False
# {'pen': 20, 'cup': 11, 'keyring': 40}
# Compra: ‘keyring’
# Cantidad pedida: 40 -> debe devolver True
# {'pen': 20, 'cup': 11, 'keyring': 40}
# Compra: ‘popcorn'
# Cantidad pedida: 5 -> debe devolver False 

# Diccionario de stock
stock = {'pen': 20, 'cup': 11, 'keyring': 40}

# Datos de la compra
compra = 'cup'  # Artículo a comprar
cantidad_pedida = 9  # Cantidad solicitada
# Comprobación directa
if compra in stock and stock[compra] >= cantidad_pedida:
    print(True)
else:
    print(False)
# Ejemplo 2
compra = 'pen'
cantidad_pedida = 21
if compra in stock and stock[compra] >= cantidad_pedida:
    print(True)
else:
    print(False)
# Ejemplo 3
compra = 'keyring'
cantidad_pedida = 40
if compra in stock and stock[compra] >= cantidad_pedida:
    print(True)
else:
    print(False)
# Ejemplo 4
compra = 'popcorn'
cantidad_pedida = 5
if compra in stock and stock[compra] >= cantidad_pedida:
    print(True)
else:
    print(False)
