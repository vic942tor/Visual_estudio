"""
Autores: Víctor Fernandez Díaz ~ Marcos Javier Pérez Gómez
"""
import csv
import os
#Obtener el directorio base y construir la ruta del archivo .csv
directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")
def cargar_datos():
    """
    Carga los datos desde el archivo CSV y los devuelve en una lista de diccionarios.
    Retorna:
    - list: Lista de diccionarios con los datos cargados.
    """
    datos = []
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as f:
            leer_csv = csv.DictReader(f)
            datos = list(leer_csv)
    except FileNotFoundError:
        print(f"Error: Archivo {archivo_csv} no encontrado.")
    return datos
def mostrar_informacion_poliza(polizas, siniestros, recibos, nro_poliza):
    """
    Muestra la información de una póliza específica, incluidos sus siniestros y recibos.
    """
    # Busca la póliza
    for poliza in polizas:
        if poliza['nro_poliza'] == nro_poliza:
            # Obtiene los siniestros asociados
            siniestros_asociados = [s for s in siniestros if s['nro_poliza'] == nro_poliza]
            # Obtiene los recibos asociados
            recibos_asociados = [r for r in recibos if r['nro_poliza'] == nro_poliza]
            
            # Muestra la información de la póliza
            print("\nInformación de la Póliza:")
            print(f"{'Número de Póliza':<20} {'Tomador':<20} {'Domicilio':<30} {'Email':<30} {'Estado':<15}")
            print("=" * 115)
            print(f"{poliza['nro_poliza']:<20} {poliza['nombre_tomador']:<20} {poliza['domicilio']:<30} {poliza['email_contacto']:<30} {poliza['estado_poliza']:<15}")
            print("=" * 115)

            # Muestra los siniestros asociados
            if siniestros_asociados:
                print("\nLista de Siniestros:")
                print(f"{'Número de Siniestro':<20} {'Descripción':<30} {'Estado':<15} {'Importe a Pagar':<20}")
                print("=" * 85)
                for s in siniestros_asociados:
                    print(f"{s['nro_siniestro']:<20} {s['descripcion']:<30} {s['estado_siniestro']:<15} {s['importe_pagar_siniestro']:<20}")
                print("=" * 85)
            else:
                print("\nNo hay siniestros asociados a esta póliza.")

            # Muestra los recibos asociados
            if recibos_asociados:
                print("\nLista de Recibos:")
                print(f"{'ID Recibo':<15} {'Estado':<15} {'Fecha de Cobro':<20} {'Importe a Pagar':<20}")
                print("=" * 70)
                for r in recibos_asociados:
                    print(f"{r['id_recibo']:<15} {r['estado_recibo']:<15} {r['fecha_cobro']:<20} {r['importe_pagar']:<20}")
                print("=" * 70)
            else:
                print("\nNo hay recibos asociados a esta póliza.")

            return

    print("Error: No se encontró la póliza especificada.")
def mostrar_informacion_liquidacion(liquidaciones, nro_liquidacion):
    """
    Muestra solo la información esencial de una liquidación específica.
    """
    # Buscar la liquidación por número
    liquidacion_encontrada = next((liquidacion for liquidacion in liquidaciones 
                                    if liquidacion['nro_liquidacion'] == nro_liquidacion), None)

    if not liquidacion_encontrada:
        print("Error: No se encontró la liquidación especificada.")
        return

    # Mostrar la información de la liquidación
    print("\nInformación de Liquidación:")
    print(f"{'Número de Liquidación':<25} {'Fecha':<15} {'Monto':<15} {'Estado':<15}")
    print("=" * 70)
    print(f"{liquidacion_encontrada['nro_liquidacion']:<25} "
          f"{liquidacion_encontrada['fecha_liquidacion']:<15} "
          f"{liquidacion_encontrada['importe_pagar']:<15} "
          f"{liquidacion_encontrada['estado_liquidacion']:<15}")
    print("=" * 70)
def menu():
    """
    Menú principal para mostrar estadísticas.
    No retorna nada, solo imprime resultados en pantalla.
    """
#Carga datos desde el archivo CSV
    datos = cargar_datos()
#Separa los datos en listas de pólizas, siniestros, recibos y liquidaciones
    polizas = [d for d in datos if 'nro_poliza' in d]
    siniestros = [d for d in datos if 'nro_siniestro' in d]
    recibos = [d for d in datos if 'id_recibo' in d]
    liquidaciones = [d for d in datos if 'nro_liquidacion' in d]
    while True:
        print("""
        Menú de Estadísticas:
        1. Mostrar información de una póliza
        2. Mostrar información de una liquidación
        0. Regresar al menú principal
        """)
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nro_poliza = input("Ingrese el número de la póliza: ")
            resultado = mostrar_informacion_poliza(polizas, siniestros, recibos, nro_poliza)
            if isinstance(resultado, dict):
                print("\nInformación de la póliza:")
                print("Póliza:", resultado["Póliza"])
                print("Siniestros:", resultado["Siniestros"])
                print("Recibos:", resultado["Recibos"])
            else:
                print(resultado)
        elif opcion == "2":
            nro_liquidacion = input("Ingrese el número de la liquidación: ")
            resultado = mostrar_informacion_liquidacion(liquidaciones, nro_liquidacion)
            if isinstance(resultado, dict):
                print("\nInformación de la liquidación:")
                for clave, valor in resultado.items():
                    print(f"{clave}: {valor}")
            else:
                print(resultado)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")