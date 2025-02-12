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
    Crea un nuevo recibo validando que el tomador exista en el CSV.
    """
    id_recibo = input("Ingrese el ID del recibo: ")
    dni = input("Ingrese el DNI del tomador: ")

    # Validar la existencia del tomador
    if not validar_tomador_existente(dni):
        print("Error: El tomador indicado no existe. Por favor, crea un tomador antes de crear un recibo.")
        return
    
    # Duplicar datos del tomador si ya existe un recibo
    tomador_existente = next((t for t in datos if t['id_tomador'] == dni), None)

    nuevo_recibo = {
        "id_recibo": id_recibo,
        "nro_poliza": input("Ingrese el número de póliza: "),
        "fecha_inicio": input("Ingrese la fecha de inicio (YYYY-MM-DD): "),
        "duracion": input("Ingrese la duración (A: Anual, S: Semestral, T: Trimestral, M: Mensual): "),
        "importe_cobrar": float(input("Ingrese el importe a cobrar: ")),
        "fecha_cobro": input("Ingrese la fecha de cobro (YYYY-MM-DD): "),
        "estado_recibo": input("Ingrese el estado del recibo (Pendiente, Pendiente_banco, Cobrado, Cobrado_banco, Baja): "),
        "importe_pagar": float(input("Ingrese el importe a pagar: ")),
        "estado_liquidacion": input("Ingrese el estado de liquidación (Pendiente, Liquidado): "),
        "fecha_liquidacion": input("Ingrese la fecha de liquidación (YYYY-MM-DD): ")
    }

    # Duplicar datos del tomador en el nuevo recibo
    if tomador_existente:
        nuevo_recibo.update({
            "id_tomador": tomador_existente['id_tomador'],
            "nombre_tomador": tomador_existente['nombre_tomador'],
            "fecha_nacimiento": tomador_existente['fecha_nacimiento'],
            "domicilio": tomador_existente['domicilio'],
            "movil_contacto": tomador_existente['movil_contacto'],
            "email_contacto": tomador_existente['email_contacto']
        })

    # Validar que todos los campos requeridos no sean None
    for key, value in nuevo_recibo.items():
        if value is None or (isinstance(value, str) and value.strip() == ""):
            print(f"Error: El campo {key} no puede estar vacío.")
            return
    
    # Agregar el recibo a los datos en memoria
    datos.append(nuevo_recibo)
    
    # Guardar en el mismo archivo CSV
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = datos[0].keys() if datos else [] 
        escribir_csv = csv.DictWriter(file, fieldnames=fieldnames)
        escribir_csv.writeheader()
        escribir_csv.writerows(datos)
    
    print("Recibo creado con éxito y almacenado en correduriadata.csv.")

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
    Lista todos los recibos cargados desde el archivo CSV.
    """
    if not datos:
        print("No hay recibos registrados.")
        return
    print("\nLista de Recibos:")
    print(f"{'ID Recibo':<15} {'Número de Póliza':<20} {'Estado':<15}")
    print("=" * 60)

    # Muestra a los recibos en una línea ordenada
    for recibo in datos:
        print(f"{recibo['id_recibo']:<15} {recibo['nro_poliza']:<20} {recibo['estado_recibo']:<15}")

    print("=" * 60)

# Menú de recibos
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

if __name__ == "__main__":
    menu()