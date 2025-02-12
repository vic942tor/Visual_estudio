"""
Autores: Víctor Fernandez Díaz ~ Marcos Javier Pérez Gómez
"""
import os
import csv

directorio_base = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(directorio_base, "correduriadata.csv")

# Cargar datos desde el archivo CSV
def cargar_datos():
    """
    Carga los datos desde el archivo CSV y los devuelve en una lista de diccionarios.
    """
    datos = []
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            leer_csv = csv.DictReader(file)
            for row in leer_csv:
                datos.append(row)
    except FileNotFoundError:
        print("Error: Archivo de datos no encontrado.")
    return datos

# Lista de datos cargados desde el CSV
datos = cargar_datos()

# Validar si un tomador existe
def validar_tomador_existente(dni):
    """
    Verifica si el DNI del tomador existe en los datos cargados desde el CSV.
    """
    return any(t['id_tomador'] == dni for t in datos)

# Crear un nuevo recibo
def crear_recibo():
    """
    Crea un nuevo recibo validando que el tomador exista en el CSV y actualiza su línea correspondiente.
    """
    id_recibo = input("Ingrese el ID del recibo: ")
    dni = input("Ingrese el DNI del tomador: ")

    # Validar la existencia del tomador
    if not validar_tomador_existente(dni):
        print("Error: El tomador indicado no existe. Por favor, crea un tomador antes de crear un recibo.")
        return

    # Buscar la línea exacta donde se encuentra el tomador en el CSV
    for recibo in datos:
        if recibo['id_tomador'] == dni:
            # Actualizar solo los datos del recibo sin duplicar al tomador
            recibo.update({
                "id_recibo": id_recibo,
                "nro_poliza": input("Ingrese el número de póliza: "),
                "fecha_inicio": input("Ingrese la fecha de inicio (YYYY-MM-DD): "),
                "duracion": input("Ingrese la duración (Anual, Semestral, Trimestral, Mensual): "),
                "importe_cobrar": float(input("Ingrese el importe a cobrar: ")),
                "fecha_cobro": input("Ingrese la fecha de cobro (YYYY-MM-DD): "),
                "estado_recibo": input("Ingrese el estado del recibo (Pendiente, Cobrado, Baja): "),
                "importe_pagar": float(input("Ingrese el importe a pagar: ")),
                "estado_liquidacion": input("Ingrese el estado de liquidación (Pendiente, Liquidado): "),
                "fecha_liquidacion": input("Ingrese la fecha de liquidación (YYYY-MM-DD): ")
            })
            break

    # Guardar cambios en el CSV
    guardar_datos()
    print("Recibo actualizado correctamente.")

# Modificar un recibo
def modificar_recibo():
    """
    Modifica el estado de un recibo existente.
    """
    listar_recibos()  # Muestra la lista de recibos antes de modificar
    id_recibo = input("Ingrese el ID del recibo a modificar: ")
    for recibo in datos:
        if recibo['id_recibo'] == id_recibo:
            print("Recibo encontrado")
            nuevo_estado = input("Ingrese el nuevo estado del recibo (Pendiente, Pendiente_banco, Cobrado, Cobrado_banco, Baja): ")
            recibo['estado_recibo'] = nuevo_estado
            guardar_datos()
            print("Recibo modificado correctamente.")
            return
    print("Recibo no encontrado.")

# Guardar datos en el archivo CSV
def guardar_datos():
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = datos[0].keys()  # Obtener los nombres de los campos
        escribir_csv = csv.DictWriter(file, fieldnames=fieldnames)
        escribir_csv.writeheader()
        escribir_csv.writerows(datos)

# Listar recibos
def listar_recibos():
    """
    Lista solo los recibos que tienen un ID de recibo registrado.
    """
    recibos_filtrados = [recibo for recibo in datos if recibo.get('id_recibo')]
    if not recibos_filtrados:
        print("No hay recibos registrados.")
        return

    print("\nLista de Recibos:")
    print(f"{'ID Recibo':<15} {'DNI Tomador':<15} {'Número de Póliza':<20} {'Estado':<15}")
    print("=" * 70)
    for recibo in recibos_filtrados:
        print(f"{recibo['id_recibo']:<15} {recibo['id_tomador']:<15} {recibo['nro_poliza']:<20} {recibo['estado_recibo']:<15}")
    print("=" * 70)
def menu():
    """
    Muestra el menú de opciones de los recibos y permite interactuar con las opciones.
    """
    while True:
        print("""
        Menú Recibos:
        1. Crear Recibo
        2. Listar Recibos
        3. Modificar Recibo
        0. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_recibo()
        elif opcion == '2':
            listar_recibos()
        elif opcion == '3':
            modificar_recibo()
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")