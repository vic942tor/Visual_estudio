import csv
import os
from Utilidades import validar_nif_nie_cif 

#Obtiene el directorio base y construye la ruta del archivo CSV donde se almacenan las pólizas
directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")
polizas = []  
def cargar_polizas():
    """Carga las pólizas desde el archivo CSV si existe."""
    global polizas
    polizas = []
    if os.path.exists(archivo_csv):
        with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
            lector_csv = csv.DictReader(file)
            for fila in lector_csv:
                if 'nro_poliza' in fila and 'id_tomador' in fila:
#Convierte los datos del vehículo de cadena a tupla
                    datos_vehiculo = fila.get('datos_vehiculo', None)
                    if datos_vehiculo:
                        datos_vehiculo = tuple(datos_vehiculo.strip("()").split(","))
                    else:
                        datos_vehiculo = ()
#Crea el diccionario de la póliza y lo agrega a la lista
                    poliza = {
                        'nro_poliza': fila['nro_poliza'],
                        'id_tomador': fila['id_tomador'],
                        'matricula': fila['matricula'],
                        'datos_vehiculo': datos_vehiculo,
                        'cobertura': fila['cobertura'],
                        'id_conductor': fila['id_conductor'],
                        'estado_poliza': fila['estado_poliza'],
                        'fecha_emision': fila['fecha_emision'],
                        'forma_pago': fila['forma_pago']
                    }
                    polizas.append(poliza)
    else:
        print("Error: El archivo de pólizas no existe.")
def guardar_polizas():
    """Guarda la lista de pólizas en el archivo CSV."""
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = polizas[0].keys() if polizas else []
        escribir_csv = csv.DictWriter(file, fieldnames=fieldnames)
        escribir_csv.writeheader()
        escribir_csv.writefilas(polizas)
def crear_poliza():
    """Solicita datos al usuario y crea una nueva póliza."""
    nro_poliza = input("Ingrese el número de póliza: ")
    if any(p['nro_poliza'] == nro_poliza for p in polizas):
        print("Error: La póliza ya existe.")
        return
    id_tomador = input("Ingrese el ID del tomador (NIF/NIE/CIF): ")
    if not validar_nif_nie_cif(id_tomador):
        print("Error: ID del tomador no válido.")
        return
#Se solicita la información del vehículo
    matricula = input("Ingrese la matrícula del vehículo: ")
    tipo_vehiculo = input("Ingrese el tipo de vehículo (Ciclomotor, Moto, Turismo, Furgoneta, Camión): ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    funcionamiento = input("Ingrese el funcionamiento (Combustión, Eléctrico, Mixto): ")
#Se define la cobertura
    cobertura = input("Ingrese la cobertura (RC, RL, INC, RB, TR, o 'normal' para RC): ")
    if cobertura == 'normal':
        cobertura = 'RC'
#Datos del conductor
    nif_conductor = input("Ingrese el NIF/NIE del conductor: ")
    fecha_nacimiento_conductor = input("Ingrese la fecha de nacimiento del conductor (YYYY-MM-DD): ")
    tipo_carnet = input("Ingrese el tipo de carnet: ")
    fecha_carnet = input("Ingrese la fecha de emisión del carnet (YYYY-MM-DD): ")
#Datos adicionales de la póliza
    estado_poliza = input("Ingrese el estado de la póliza (Cobrada, PteCobro, Baja): ")
    fecha_emision = input("Ingrese la fecha de emisión (YYYY-MM-DD): ")
    forma_pago = input("Ingrese la forma de pago (Efectivo o Banco): ")
#Se almacena la nueva póliza en la lista
    poliza = {
        'nro_poliza': nro_poliza,
        'id_tomador': id_tomador,
        'matricula': matricula,
        'datos_vehiculo': (tipo_vehiculo, marca, modelo, funcionamiento),
        'cobertura': cobertura,
        'id_conductor': (nif_conductor, fecha_nacimiento_conductor, tipo_carnet, fecha_carnet),
        'estado_poliza': estado_poliza,
        'fecha_emision': fecha_emision,
        'forma_pago': forma_pago
    }
    polizas.append(poliza)
    guardar_polizas()
    print("Póliza creada exitosamente.")
def modificar_poliza():
    """Permite modificar los datos de una póliza existente."""
    nro_poliza = input("Ingrese el número de póliza a modificar: ")
    for poliza in polizas:
        if poliza['nro_poliza'] == nro_poliza:
            print("Póliza encontrada:", poliza)
#Se actualizan los valores de la póliza con la nueva información ingresada
            poliza['id_tomador'] = input("Ingrese el nuevo ID del tomador: ")
            poliza['matricula'] = input("Ingrese la nueva matrícula del vehículo: ")
            poliza['datos_vehiculo'] = (
                input("Ingrese el nuevo tipo de vehículo: "),
                input("Ingrese la nueva marca del vehículo: "),
                input("Ingrese el nuevo modelo del vehículo: "),
                input("Ingrese el nuevo funcionamiento: ")
            )
            poliza['cobertura'] = input("Ingrese la nueva cobertura: ")
            poliza['id_conductor'] = (
                input("Ingrese el nuevo NIF/NIE del conductor: "),
                input("Ingrese la nueva fecha de nacimiento del conductor: "),
                input("Ingrese el nuevo tipo de carnet: "),
                input("Ingrese la nueva fecha de emisión del carnet: ")
            )
            poliza['estado_poliza'] = input("Ingrese el nuevo estado de la póliza: ")
            poliza['fecha_emision'] = input("Ingrese la nueva fecha de emisión: ")
            poliza['forma_pago'] = input("Ingrese la nueva forma de pago: ")
            guardar_polizas()
            print("Póliza modificada exitosamente.")
            return
    print("Póliza no encontrada.")
def eliminar_poliza():
    """Elimina una póliza del sistema."""
    nro_poliza = input("Ingrese el número de póliza a eliminar: ")
    global polizas
    polizas = [p for p in polizas if p['nro_poliza'] != nro_poliza]
    guardar_polizas()
    print("Póliza eliminada exitosamente.")
def listar_polizas():
    """Muestra todas las pólizas almacenadas."""
    if not polizas:
        print("No hay pólizas registradas.")
        return
    print("\nLista de Pólizas:")
    for poliza in polizas:
        print(f"Número de Póliza: {poliza['nro_poliza']}, "
              f"ID Tomador: {poliza['id_tomador']}, "
              f"Matrícula: {poliza['matricula']}, "
              f"Estado: {poliza['estado_poliza']}, "
              f"Fecha de Emisión: {poliza['fecha_emision']}, "
              f"Forma de Pago: {poliza['forma_pago']}")
def menu():
    """Muestra el menú de gestión de pólizas y permite interactuar con las opciones."""
    cargar_polizas()
    while True:
        print("\nMenú de Pólizas")
        print("1. Crear Póliza")
        print("2. Modificar Póliza")
        print("3. Eliminar Póliza")
        print("4. Listar Pólizas")
        print("5. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_poliza()
        elif opcion == '2':
            modificar_poliza()
        elif opcion == '3':
            eliminar_poliza()
        elif opcion == '4':
            listar_polizas()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
cargar_polizas()
