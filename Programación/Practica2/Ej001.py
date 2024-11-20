# Una empresa que se dedica a la comercialización de productos, desea actualizar
# su sistema de datos con una nueva estructura de datos basada en diccionarios.
# Para ello, le han contratado para generar un programa en Python que cree esa
# estructura y pueda acceder a los datos que en ella se almacene.

CATEGORIAS = ('frío', 'verduras', 'carnes', 'panadería', 'bazar', 'despensa', 'winos', 'lácteos')
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
#Valida el código
        while True:
            codigo_numero = input('Introduzca el número del código del producto, debe tener 4 digitos: ')
            if len(codigo_numero) > 4 or len(codigo_numero) < 4 or codigo_numero.isalpha():
                print('Este código no es valido, porfavor vuelva a introducirlo')
                continue
            break          
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
        while True:
            try:
                cantidad = float(input('Introduzca la cantidad del producto: '))
            except:
                print('Por favor, debe establecer la cantidad del producto')
                continue
            if cantidad < 0:
                print("La cantidad introducida no puede ser negativa.")
                continue
            break
        while True:
            try:
                precio = float(input('Introduzca el precio del producto: '))
            except:
                print('Por favor, debe establecer el precio del producto')
                continue
            if precio == '':
                print('Por favor, debe establecer el precio del producto')
            if precio < 0:
                print("El precio introducido no puede ser negativo.")
                continue
            break
#Almacena el producto en el diccionario bajo el tipo y código correspondientes
        productos[tipo_producto][codigo] = [descripcion, round(cantidad, 2), round(precio, 2)]
#Muestra los productos almacenados
print("\nProductos almacenados:")
for tipo, productos_tipo in productos.items():
    print(f"\nTipo de producto: {tipo}")
    for codigo, detalles in productos_tipo.items():
        descripcion, cantidad, precio = detalles
        print(f"Código: {codigo}")
        print(f"Descripción: {descripcion}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio: {precio:.2f}€")

    


