productos = { 
    'frio': {'f0001': ['muslos pollo', 20, 8.5],
             'f0002': ['carne cerdo', 20, 5.6]},
    'verduras': {'v0001': ['tomates', 30, 2.5],
                 'v0002': ['cebollas', 20, 2.2]},
    'bazar': {'b0001': ['pala basura', 10, 3.75],
              'b0002': ['lejia', 10, 1.85]},
    'lacteos': {'l0001': ['leche entera', 50, 1.15],
                'l0002': ['leche sin lactosa', 20, 1.5]}
}

empresa01 = [
    ('verduras', 'tomates', 20, 2.15),
    ('frío', 'muslos pollo', 30, 8.65),
    ('lácteos', 'leche semidesnatada', 20, 1.4),
    ('wino', 'vino tinto monje', 10, 13.75),
    ('wino', 'vino dulce', 5, 12.15)
]

empresa02 = [
    ('pepinos', 20, 1.95),
    ('pala', 5, 3.80),
    ('leche entera', 10, 1.90),
    ('pan mediano', 20, 0.5),
    ('vino blanco', 5, 14.25)
]

CATEGORIAS = ('frío', 'verduras', 'carnes', 'panadería', 'bazar', 'despensa', 'winos', 'lácteos')

# Procesar empresa01
for tipo_producto, descripcion, cantidad, precio in empresa01:
    tipo_producto = tipo_producto.lower()
    if tipo_producto not in productos:
        productos[tipo_producto] = {}
    encontrado = False
    # Buscar en la categoría del producto
    for codigo, detalles in productos[tipo_producto].items():
        if detalles[0].lower() == descripcion.lower():
            # Actualizar cantidad y precio
            productos[tipo_producto][codigo][1] += cantidad
            productos[tipo_producto][codigo][2] = max(precio, detalles[2])
            encontrado = True
            break
    # Si no existe el producto, crear uno nuevo
    if not encontrado:
        while True:
            codigo_numero = input(f'Introduzca un número de código para "{descripcion}" (4 dígitos): ')
            if len(codigo_numero) == 4 and codigo_numero.isdigit():
                break
            print('Código inválido. Intente nuevamente.')
        codigo = tipo_producto[0].upper() + codigo_numero
        productos[tipo_producto][codigo] = [descripcion, cantidad, precio]

# Procesar empresa02
for descripcion, cantidad, precio in empresa02:
    encontrado = False
    # Buscar en todas las categorías
    for tipo_producto, productos_tipo in productos.items():
        for codigo, detalles in productos_tipo.items():
            if detalles[0].lower() == descripcion.lower():
                # Actualizar cantidad y precio
                detalles[1] += cantidad
                detalles[2] = max(precio, detalles[2])
                encontrado = True
                break
        if encontrado:
            break
    # Si no se encuentra el producto, crear uno nuevo
    if not encontrado:
        while True:
            tipo_producto = input(f'Introduzca el tipo de producto para "{descripcion}" (opciones: {", ".join(CATEGORIAS)}): ').lower()
            if tipo_producto in productos:
                break
            print('Tipo de producto inválido. Intente nuevamente.')
        while True:
            codigo_numero = input(f'Introduzca un número de código para "{descripcion}" (4 dígitos): ')
            if len(codigo_numero) == 4 and codigo_numero.isdigit():
                break
            print('Código inválido. Intente nuevamente.')
        codigo = tipo_producto[0].upper() + codigo_numero
        productos[tipo_producto][codigo] = [descripcion, cantidad, precio]

# Mostrar los productos finales
print("\nProductos actualizados:")
for tipo_producto, productos_tipo in productos.items():
    print(f"\nTipo de producto: {tipo_producto.capitalize()}")
    for codigo, detalles in productos_tipo.items():
        descripcion, cantidad, precio = detalles
        print(f"Código: {codigo}")
        print(f"Descripción: {descripcion}")
        print(f"Cantidad: {cantidad:.2f}")
        print(f"Precio: {precio:.2f}€")
