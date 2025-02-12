import csv
import os
from Utilidades import validar_nif_nie_cif

#Obtener el directorio base y construir la ruta del archivo CSV
directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")
polizas = []
def cargar_polizas():
    """Carga las pólizas desde el archivo CSV."""
    if os.path.exists(archivo_csv):
        with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
#Convertir datos de la póliza
                row['datos_vehiculo'] = eval(row['datos_vehiculo'])
                row['id_conductor'] = eval(row['id_conductor'])
                polizas.append(row)
def guardar_polizas():
    """Guarda las pólizas en el archivo CSV."""
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = polizas[0].keys() if polizas else []
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(polizas)
def crear_poliza():
    """Crea una nueva póliza."""
    nro_poliza = input("Ingrese el número de póliza: ")
    if any(p['nro_poliza'] == nro_poliza for p in polizas):
        print("Error: La póliza ya existe.")
        return
    id_tomador = input("Ingrese el ID del tomador (NIF/NIE/CIF): ")
    if not validar_nif_nie_cif(id_tomador):
        print("Error: ID del tomador no válido.")
        return
    matricula = input("Ingrese la matrícula del vehículo: ")
    tipo_vehiculo = input("Ingrese el tipo de vehículo (Ciclomotor, Moto, Turismo, Furgoneta, Camión): ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    funcionamiento = input("Ingrese el funcionamiento (Combustión, Eléctrico, Mixto): ")
#Cobertura
    cobertura = input("Ingrese la cobertura (RC, RL, INC, RB, TR, o 'normal' para RC): ")
    if cobertura == 'normal':
        cobertura = 'RC'
#Datos del conductor
    nif_conductor = input("Ingrese el NIF/NIE del conductor: ")
    fecha_nacimiento_conductor = input("Ingrese la fecha de nacimiento del conductor (YYYY-MM-DD): ")
    tipo_carnet = input("Ingrese el tipo de carnet: ")
    fecha_carnet = input("Ingrese la fecha de emisión del carnet (YYYY-MM-DD): ")
    estado_poliza = input("Ingrese el estado de la póliza (Cobrada, PteCobro, Baja): ")
    fecha_emision = input("Ingrese la fecha de emisión (YYYY-MM-DD): ")
    forma_pago = input("Ingrese la forma de pago (Efectivo o Banco): ")
#Crear la póliza
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
    """Modifica una póliza existente."""
    nro_poliza = input("Ingrese el número de póliza a modificar: ")
    for poliza in polizas:
        if poliza['nro_poliza'] == nro_poliza:
            print("Póliza encontrada:", poliza)
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
    """Elimina una póliza existente."""
    nro_poliza = input("Ingrese el número de póliza a eliminar: ")
    global polizas
    polizas = [p for p in polizas if p['nro_poliza'] != nro_poliza]
    guardar_polizas()
    print("Póliza eliminada exitosamente.")
def menu():
    """Función que muestra el menú de pólizas y gestiona las opciones seleccionadas."""
    cargar_polizas()
    while True:
        print("\nMenú de Pólizas")
        print("1. Crear Póliza")
        print("2. Modificar Póliza")
        print("3. Eliminar Póliza")
        print("4. Regresar al menú principal")
        option = input("Seleccione una opción: ")
        if option == '1':
            crear_poliza()
        elif option == '2':
            modificar_poliza()
        elif option == '3':
            eliminar_poliza()
        elif option == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
cargar_polizas()




