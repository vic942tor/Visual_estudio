import csv
import os

# Definir la ruta del archivo CSV
directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")

# Cargar datos desde el archivo CSV
def cargar_datos():
    datos = []
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            leer_csv = csv.DictReader(file)
            for row in leer_csv:
                datos.append(row)
    except FileNotFoundError:
        print("Error: Archivo de datos no encontrado.")
    return datos

# Guardar datos en el archivo CSV
def guardar_datos(datos):
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
        nombre_campos = datos[0].keys()  # Obtener los nombres de los campos
        escribir_csv = csv.DictWriter(file, nombre_campos=nombre_campos)
        escribir_csv.writeheader()
        escribir_csv.writerows(datos)

# Crear un nuevo siniestro
def crear_siniestro(datos):
    nro_siniestro = input("Ingrese el número de siniestro (formato aaaanro_correlativo): ")
    
    # Verificar que el siniestro no exista
    if any(s['nro_siniestro'] == nro_siniestro for s in datos):
        print("El siniestro con este número ya existe.")
        return

    nro_poliza = input("Ingrese el número de la póliza asociada: ")
    
    # Verificar que la póliza exista
    if not any(p['nro_poliza'] == nro_poliza for p in datos):
        print("La póliza con ese número no existe.")
        return

    descripcion = input("Ingrese una descripción del siniestro: ")
    matricula_contrario = input("Ingrese la matrícula del vehículo contrario: ")
    compania_contrario = input("Ingrese la compañía aseguradora del contrario: ")
    nro_poliza_contrario = input("Ingrese el número de la póliza del contrario: ")
    importe_pagar = float(input("Ingrese el importe a pagar: "))  # Nuevo campo
    estado_siniestro = input("Ingrese el estado del siniestro: ")  # Nuevo campo
    fecha_abono = input("Ingrese la fecha de abono (YYYY-MM-DD): ")  # Nuevo campo
    estado_liquidacion = 'Pendiente'  # Valor por defecto
    fecha_liquidacion = None  # Valor por defecto

    # Completamos el nuevo siniestro
    siniestro = {
        'nro_siniestro': nro_siniestro,
        'nro_poliza': nro_poliza,
        'descripcion': descripcion,
        'matricula_contrario': matricula_contrario,
        'compania_contrario': compania_contrario,
        'nro_poliza_contrario': nro_poliza_contrario,
        'importe_pagar': importe_pagar,
        'estado_siniestro': estado_siniestro,
        'fecha_abono': fecha_abono,
        'estado_liquidacion': estado_liquidacion,
        'fecha_liquidacion': fecha_liquidacion
    }

    # Agregar el siniestro a la lista de siniestros
    datos.append(siniestro)
    print(f"Siniestro {nro_siniestro} creado correctamente.")

    # Guardar todos los datos en el CSV
    guardar_datos(datos)

# Modificar un siniestro
def modificar_siniestro(datos):
    nro_siniestro = input("Ingrese el número de siniestro a modificar: ")
    for siniestro in datos:
        if siniestro['nro_siniestro'] == nro_siniestro:
            print("Siniestro encontrado:", siniestro)
            siniestro['descripcion'] = input("Ingrese la nueva descripción del siniestro: ")
            siniestro['matricula_contrario'] = input("Ingrese la nueva matrícula del vehículo contrario: ")
            siniestro['compania_contrario'] = input("Ingrese la nueva compañía aseguradora del contrario: ")
            siniestro['nro_poliza_contrario'] = input("Ingrese el nuevo número de la póliza del contrario: ")
            siniestro['importe_pagar'] = float(input("Ingrese el nuevo importe a pagar: "))
            siniestro['estado_siniestro'] = input("Ingrese el nuevo estado del siniestro: ")
            siniestro['fecha_abono'] = input("Ingrese la nueva fecha de abono (YYYY-MM-DD): ")
            guardar_datos(datos)
            print("Siniestro modificado correctamente.")
            return
    print("Siniestro no encontrado.")

# Eliminar un siniestro
def eliminar_siniestro(datos):
    nro_siniestro = input("Ingrese el número de siniestro a eliminar: ")
    datos[:] = [s for s in datos if s['nro_siniestro'] != nro_siniestro]  # Modificar la lista en su lugar
    guardar_datos(datos)
    print("Siniestro eliminado correctamente.")

# Listar siniestros
def listar_siniestros(datos):
    if not datos:
        print("No hay siniestros registrados.")
        return
    print("\nLista de Siniestros:")
    for siniestro in datos:
        print(f"Número de Siniestro: {siniestro['nro_siniestro']}, Descripción: {siniestro['descripcion']}, Estado: {siniestro['estado_siniestro']}")

# Cargar datos al inicio
datos = cargar_datos()
def menu():
    """
    Muestra el menú de opciones para la gestión de siniestros.
    """
    while True:
        print("""
        Menú de Siniestro:
        1. Crear un siniestro
        2. Modificar un siniestro
        3. Eliminar un siniestro
        4. Listar siniestros
        0. Volver al menú principal
        """)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_siniestro(datos)
        elif opcion == '2':
            modificar_siniestro(datos)
        elif opcion == '3':
            eliminar_siniestro(datos)
        elif opcion == '4':
            listar_siniestros(datos)
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")