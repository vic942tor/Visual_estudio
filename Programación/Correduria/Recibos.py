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

# Validar si una póliza existe
def validar_poliza_existente(nro_poliza):
    """
    Verifica si el número de póliza existe en los datos cargados desde el CSV.
    """
    return any(p['nro_poliza'] == nro_poliza for p in datos)

# Crear un nuevo recibo
def crear_recibo():
    """
    Crea un nuevo recibo validando que la póliza exista en el CSV.
    """
    id_recibo = input("Ingrese el ID del recibo: ")
    nro_poliza = input("Ingrese el número de póliza: ")

    # Validar la existencia de la póliza
    if not validar_poliza_existente(nro_poliza):
        print("Error: La póliza indicada no existe en la base de datos.")
        return
    
    nuevo_recibo = {
        "id_recibo": id_recibo,
        "nro_poliza": nro_poliza,
        "fecha_inicio": input("Ingrese la fecha de inicio (YYYY-MM-DD): "),
        "duracion": input("Ingrese la duración (A: Anual, S: Semestral, T: Trimestral, M: Mensual): "),
        "importe_cobrar": float(input("Ingrese el importe a cobrar: ")),
        "fecha_cobro": input("Ingrese la fecha de cobro (YYYY-MM-DD): "),
        "estado_recibo": input("Ingrese el estado del recibo (Pendiente, Pendiente_banco, Cobrado, Cobrado_banco, Baja): "),
        "importe_pagar": float(input("Ingrese el importe a pagar: ")),
        "estado_liquidacion": input("Ingrese el estado de liquidación (Pendiente, Liquidado): "),
        "fecha_liquidacion": input("Ingrese la fecha de liquidación (YYYY-MM-DD): ")
    }
    
    # Validar que todos los campos requeridos no sean None
    for key, value in nuevo_recibo.items():
        if value is None or (isinstance(value, str) and value.strip() == ""):
            print(f"Error: El campo {key} no puede estar vacío.")
            return
    
    # Agregar el recibo a los datos en memoria
    datos.append(nuevo_recibo)
    
    # Guardar en el mismo archivo CSV
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        nombre_campos = datos[0].keys() if datos else [] 
        escribir_csv = csv.DictWriter(file, nombre_campos=nombre_campos)
        escribir_csv.writeheader()
        escribir_csv.writerows(datos)
    
    print("Recibo creado con éxito y almacenado en correduriadata.csv.")

# Listar recibos
def listar_recibos():
    """
    Lista todos los recibos cargados desde el archivo CSV.
    """
    if not datos:
        print("No hay recibos registrados.")
        return
    print("\nLista de Recibos:")
    for recibo in datos:
        print(f"ID Recibo: {recibo['id_recibo']}, Número de Póliza: {recibo['nro_poliza']}, Estado: {recibo['estado_recibo']}")

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
        0. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_recibo()
        elif opcion == '2':
            listar_recibos()
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")