
import csv
import os
# Lista para almacenar las pólizas
polizas = []
# Cargar pólizas desde el archivo CSV al iniciar el programa
def cargar_polizas():
    """Carga las pólizas desde un archivo CSV."""
    if os.path.exists('polizas.csv'):
        with open('polizas.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convertir los datos de la póliza a los tipos correctos
                row['datos_vehiculo'] = eval(row['datos_vehiculo'])  # Convertir de string a tupla
                row['id_conductor'] = eval(row['id_conductor'])  # Convertir de string a tupla
                polizas.append(row)
def menu():
    """Función que muestra el menú de pólizas y gestiona las opciones seleccionadas."""
    cargar_polizas()  # Cargar pólizas al iniciar el menú
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
def crear_poliza():
    """Función para crear una nueva póliza."""
    nro_poliza = input("Ingrese el número de póliza: ")
    if any(p['nro_poliza'] == nro_poliza for p in polizas):
        print("Error: La póliza ya existe.")
        return

    id_tomador = input("Ingrese el ID del tomador: ")
    matricula = input("Ingrese la matrícula del vehículo: ")
    datos_vehiculo = (
        input("Ingrese el tipo de vehículo (Ciclomotor, Moto, Turismo, Furgoneta, Camión): "),
        input("Ingrese la marca del vehículo: "),
        input("Ingrese el modelo del vehículo: "),
        input("Ingrese el funcionamiento (Combustión, Eléctrico, Mixto): ")
    )
    cobertura = input("Ingrese la cobertura (RC, RL, INC, RB, TR): ")
    id_conductor = (
        input("Ingrese el NIF/NIE del conductor: "),
        input("Ingrese la fecha de nacimiento del conductor: "),
        input("Ingrese el tipo de carnet: "),
        input("Ingrese la fecha de emisión del carnet: ")
    )
    estado_poliza = input("Ingrese el estado de la póliza (Cobrada, PteCobro, Baja): ")
    fecha_emision = input("Ingrese la fecha de emisión: ")
    forma_pago = input("Ingrese la forma de pago (Efectivo o Banco): ")
    poliza = {
        'nro_poliza': nro_poliza,
        'id_tomador': id_tomador,
        'matricula': matricula,
        'datos_vehiculo': datos_vehiculo,
        'cobertura': cobertura,
        'id_conductor': id_conductor,
        'estado_poliza': estado_poliza,
        'fecha_emision': fecha_emision,
        'forma_pago': forma_pago
    }
    polizas.append(poliza)
    guardar_polizas()
    print("Póliza creada exitosamente.")
def modificar_poliza():
    """Función para modificar una póliza existente."""
    nro_poliza = input("Ingrese el número de póliza a modificar: ")
    for poliza in polizas:
        if poliza['nro_poliza'] == nro_poliza:
            print("Póliza encontrada:", poliza)
            poliza['id_tomador'] = input("Ingrese el nuevo ID del tomador: ")
            poliza['matricula'] = input("Ingrese la nueva matrícula del vehículo: ")
            poliza['datos_vehiculo'] = (
                input("Ingrese el nuevo tipo de vehículo (Ciclomotor, Moto, Turismo, Furgoneta, Camión): "),
                input("Ingrese la nueva marca del vehículo: "),
                input("Ingrese el nuevo modelo del vehículo: "),
                input("Ingrese el nuevo funcionamiento (Combustión, Eléctrico, Mixto): ")
            )
            poliza['cobertura'] = input("Ingrese la nueva cobertura (RC, RL, INC, RB, TR): ")
            poliza['id_conductor'] = (
                input("Ingrese el nuevo NIF/NIE del conductor: "),
                input("Ingrese la nueva fecha de nacimiento del conductor: "),
                input("Ingrese el nuevo tipo de carnet: "),
                input("Ingrese la nueva fecha de emisión del carnet: ")
            )
            poliza['estado_poliza'] = input("Ingrese el nuevo estado de la póliza (Cobrada, PteCobro, Baja): ")
            poliza['fecha_emision'] = input("Ingrese la nueva fecha de emisión: ")
            poliza['forma_pago'] = input("Ingrese la nueva forma de pago (Efectivo o Banco): ")
            guardar_polizas()
            print("Póliza modificada exitosamente.")
            return
    print("Póliza no encontrada.")
def eliminar_poliza():
    """Función para eliminar una póliza existente."""
    nro_poliza = input("Ingrese el número de póliza a eliminar: ")
    global polizas
    polizas = [p for p in polizas if p['nro_poliza'] != nro_poliza]
    guardar_polizas()
    print("Póliza eliminada exitosamente.")
def guardar_polizas():
    """Función para guardar las pólizas en un archivo CSV."""
    with open('polizas.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=polizas[0].keys())
        writer.writeheader()
        writer.writerows(polizas)

# Cargar pólizas al iniciar el módulo
cargar_polizas()




