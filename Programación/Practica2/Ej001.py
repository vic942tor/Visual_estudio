# Una empresa que se dedica a la comercialización de productos, desea actualizar
# su sistema de datos con una nueva estructura de datos basada en diccionarios.
# Para ello, le han contratado para generar un programa en Python que cree esa
# estructura y pueda acceder a los datos que en ella se almacene.

CATEGORIAS = ('frío', 'verduras', 'carnes', 'panadería', 'bazar', 'despensa', 'vinos', 'lácteos')
productos = {}
print(f'Tipos de productos disponibles: {", ".join(CATEGORIAS)}')
while True:
    tipo_producto = input('Introduzca el tipo de producto (presione Enter para finalizar): ').lower()
    if tipo_producto == "":
        break
    if tipo_producto not in CATEGORIAS:
        print('Este producto no es valido, porfavor introduzca uno valido')
        continue
    else:
        productos[tipo_producto] = {}
    codigo_numero = input('Introduzca el número del código del producto: ')
    #Genera el código del producto (primera letra del tipo de producto + número de código)
    codigo = tipo_producto[0].upper() + codigo_numero
    if codigo in productos[tipo_producto]:
        print(f'El código {codigo} ya está en uso.')
        #Si el código ya existe, se modifican cantidad y precio
        cantidad = float(input(f'Introduzca la cantidad para el producto con código {codigo}: '))
        precio = float(input(f'Introduzca el precio para el producto con código {codigo}: '))
        #Actualiza cantidad y precio en el diccionario
        productos[tipo_producto][codigo][1] += cantidad 
        productos[tipo_producto][codigo][2] = round(precio, 2)
    else:
        descripcion = input('Introduzca la descripción del producto: ')
        cantidad = float(input('Introduzca la cantidad del producto: '))
        precio = float(input('Introduzca el precio del producto: '))
        #Almacena el producto en el diccionario bajo el tipo y código correspondientes
        productos[tipo_producto][codigo] = [descripcion, cantidad, round(precio, 2)]
#Muestra los productos almacenados
print("\nProductos almacenados:")
for tipo, productos_tipo in productos.items():
    print(f"\nTipo de producto: {tipo}")
    for codigo, detalles in productos_tipo.items():
        descripcion, cantidad, precio = detalles
        print(f"Código: {codigo}")
        print(f"Descripción: {descripcion}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio: {precio}€")

    


