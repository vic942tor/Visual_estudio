import csv
import os

directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")

def cargar_datos():
    datos = []
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            datos = list(reader)
    except FileNotFoundError:
        pass
    return datos

def guardar_datos(datos):
    if datos:
        with open(archivo_csv, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)

def crear_poliza(datos, nueva_poliza):
    for poliza in datos:
        if poliza['nro_poliza'] == nueva_poliza['nro_poliza']:
            return "Error: El número de póliza ya existe."
    datos.append(nueva_poliza)
    guardar_datos(datos)
    return "Póliza creada exitosamente."

def modificar_poliza(datos, nro_poliza, nuevos_datos):
    for poliza in datos:
        if poliza['nro_poliza'] == nro_poliza:
            for clave, valor in nuevos_datos.items():
                if clave != 'nro_poliza':
                    poliza[clave] = valor
            guardar_datos(datos)
            return "Póliza modificada exitosamente."
    return "Error: No se encontró la póliza especificada."

def eliminar_poliza(datos, nro_poliza):
    for poliza in datos:
        if poliza['nro_poliza'] == nro_poliza:
            if poliza['estado_poliza'] != 'Baja':
                return "Error: No se puede eliminar una póliza vigente."
            datos.remove(poliza)
            guardar_datos(datos)
            return "Póliza eliminada exitosamente."
    return "Error: No se encontró la póliza especificada."

def listar_polizas(datos):
    return [{
        'nro_poliza': p['nro_poliza'],
        'id_tomador': p['id_tomador'],
        'matricula': p['matricula'],
        'estado_poliza': p['estado_poliza']
    } for p in datos]

def buscar_poliza(datos, nro_poliza):
    for poliza in datos:
        if poliza['nro_poliza'] == nro_poliza:
            return poliza
    return "Error: No se encontró la póliza especificada."

def menu_polizas():
    datos = cargar_datos()
    while True:
        print("\n--- Menú de Pólizas ---")
        print("1. Crear Póliza")
        print("2. Modificar Póliza")
        print("3. Eliminar Póliza")
        print("4. Listar Pólizas")
        print("5. Buscar Póliza")
        print("9. Volver al Menú Principal")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nro_poliza = input("Número de póliza: ")
            id_tomador = input("ID del tomador: ")
            matricula = input("Matrícula del vehículo: ")
            estado = input("Estado de la póliza (Cobrada/PteCobro/Baja): ")
            nueva_poliza = {"nro_poliza": nro_poliza, "id_tomador": id_tomador, "matricula": matricula, "estado_poliza": estado}
            print(crear_poliza(datos, nueva_poliza))
        elif opcion == "2":
            nro_poliza = input("Número de póliza a modificar: ")
            nuevos_datos = {}
            matricula = input("Nueva matrícula (o enter para no cambiar): ")
            if matricula:
                nuevos_datos["matricula"] = matricula
            estado = input("Nuevo estado de la póliza (o enter para no cambiar): ")
            if estado:
                nuevos_datos["estado_poliza"] = estado
            print(modificar_poliza(datos, nro_poliza, nuevos_datos))
        elif opcion == "3":
            nro_poliza = input("Número de póliza a eliminar: ")
            print(eliminar_poliza(datos, nro_poliza))
        elif opcion == "4":
            for p in listar_polizas(datos):
                print(p)
        elif opcion == "5":
            nro_poliza = input("Número de póliza a buscar: ")
            print(buscar_poliza(datos, nro_poliza))
        elif opcion == "9":
            break
        else:
            print("Opción no válida.")