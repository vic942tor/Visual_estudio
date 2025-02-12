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
            reader = csv.DictReader(file)
            for row in reader:
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
    
    # Agregar el recibo a los datos en memoria
    datos.append(nuevo_recibo)
    
    # Guardar en el mismo archivo CSV
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = datos[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(datos)
    
    print("Recibo creado con éxito y almacenado en correduriadata.csv.")

# Menú de recibos
def menu():
    """
    Muestra el menú de opciones de los recibos y permite interactuar con las opciones.
    """
    while True:
        print("""
        Menú Recibos:
        1. Crear Recibo
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_recibo()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")