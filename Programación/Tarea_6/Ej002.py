import json
import os

directorio_script = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_JSON = os.path.join(directorio_script, "inventario.json")

class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"ID: {self.id_producto} | {self.nombre} - ${self.precio:.2f}"
    def __eq__(self, other):
        return isinstance(other, Producto) and self.id_producto == other.id_producto
class Inventariable:
    def __init__(self, stock):
        self.stock = max(0, stock)
    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
    def vender(self, cantidad):
        if 0 < cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False
    def __str__(self):
        return f"Stock: {self.stock} unidades"
class Electronico(Producto, Inventariable):
    def __init__(self, id_producto, nombre, precio, stock, garantia):
        Producto.__init__(self, id_producto, nombre, precio)
        Inventariable.__init__(self, stock)
        self.garantia = garantia
    def __str__(self):
        return super().__str__() + f" | Garantía: {self.garantia} meses | {Inventariable.__str__(self)}"
class Ropa(Producto, Inventariable):
    def __init__(self, id_producto, nombre, precio, stock, talla, material):
        Producto.__init__(self, id_producto, nombre, precio)
        Inventariable.__init__(self, stock)
        self.talla = talla
        self.material = material
    def __str__(self):
        return super().__str__() + f" | Talla: {self.talla} | Material: {self.material} | {Inventariable.__str__(self)}"
class Alimento(Producto, Inventariable):
    def __init__(self, id_producto, nombre, precio, stock, fecha_expiracion):
        Producto.__init__(self, id_producto, nombre, precio)
        Inventariable.__init__(self, stock)
        self.fecha_expiracion = fecha_expiracion
    def __str__(self):
        return super().__str__() + f" | Expira: {self.fecha_expiracion} | {Inventariable.__str__(self)}"
inventario = []
CLASES_PRODUCTO = {
    "Electronico": Electronico,
    "Ropa": Ropa,
    "Alimento": Alimento
}
def guardar_inventario():
    with open(ARCHIVO_JSON, "w") as file:
        json.dump([prod.__dict__ for prod in inventario], file, indent=4)
def cargar_inventario():
    global inventario
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r") as file:
            data = json.load(file)
            inventario = []
            for item in data:
                clase = CLASES_PRODUCTO.get(item.pop("__class__", ""), Producto)
                inventario.append(clase(**item))
def agregar_producto():
    opciones = {"1": Electronico, "2": Ropa, "3": Alimento}
    tipo = input("Tipo (1. Electrónico, 2. Ropa, 3. Alimento): ")
    if tipo not in opciones:
        print("Opción inválida.")
        return
    id_producto = int(input("ID: "))
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))
    if tipo == "1":
        garantia = int(input("Garantía (meses): "))
        producto = Electronico(id_producto, nombre, precio, stock, garantia)
    elif tipo == "2":
        talla = input("Talla: ")
        material = input("Material: ")
        producto = Ropa(id_producto, nombre, precio, stock, talla, material)
    else:
        fecha_expiracion = input("Fecha de expiración (YYYY-MM-DD): ")
        producto = Alimento(id_producto, nombre, precio, stock, fecha_expiracion)
    inventario.append(producto)
    guardar_inventario()
    print("Producto agregado exitosamente.")
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    for prod in inventario:
        print(prod)
def actualizar_stock():
    id_producto = int(input("ID del producto: "))
    cantidad = int(input("Cantidad a agregar: "))
    for prod in inventario:
        if prod.id_producto == id_producto:
            prod.agregar_stock(cantidad)
            guardar_inventario()
            print("Stock actualizado.")
            return
    print("Producto no encontrado.")
def vender_producto():
    id_producto = int(input("ID del producto: "))
    cantidad = int(input("Cantidad a vender: "))
    for prod in inventario:
        if prod.id_producto == id_producto:
            if prod.vender(cantidad):
                print("Venta realizada.")
                if prod.stock == 0:
                    inventario.remove(prod)
                guardar_inventario()
                return
            print(f"Stock insuficiente. Disponible: {prod.stock}")
            return
    print("Producto no encontrado.")
def buscar_producto():
    criterio = input("Buscar por (1. Nombre, 2. Categoría): ")
    termino = input("Ingrese el término de búsqueda: ").strip().lower()
    if not termino:
        print("Debe ingresar un término de búsqueda.")
        return
    encontrados = [
        prod for prod in inventario
        if (criterio == "1" and termino in prod.nombre.lower()) or
           (criterio == "2" and termino in prod.__class__.__name__.lower())
    ]
    if encontrados:
        for prod in encontrados:
            print(prod)
    else:
        print("No se encontraron productos.")
cargar_inventario()
while True:
    print("\n1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Actualizar stock")
    print("4. Vender producto")
    print("5. Buscar producto")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        actualizar_stock()
    elif opcion == "4":
        vender_producto()
    elif opcion == "5":
        buscar_producto()
    elif opcion == "6":
        break
    else:
        print("Opción no válida.")
