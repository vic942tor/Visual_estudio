import csv
import os
from datetime import datetime

#Obtiene el directorio base y construir la ruta del archivo .csv
directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")
def cargar_datos():
    """
    Carga los datos desde el archivo CSV y los devuelve en una lista de diccionarios.
    
    Retorna:
        list: Lista de diccionarios con los datos cargados.
    """
    datos = []
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as f:
            lector_csv = csv.DictReader(f)
            datos = list(lector_csv)
    except FileNotFoundError:
        print("Error: Archivo de datos no encontrado.")
    return datos
def guardar_datos(datos):
    """
    Guarda los datos en el archivo CSV.
    Parámetros:
        datos (list): Lista de diccionarios con los datos a guardar.
    """
    if datos:
        with open(archivo_csv, "w", newline='', encoding='utf-8') as f:
#Usa las claves del primer diccionario como encabezados
            fieldnames = datos[0].keys()  
            escribir_csv = csv.DictWriter(f, fieldnames=fieldnames)
            escribir_csv.writeheader()
            escribir_csv.writerows(datos)
def mostrar_tomadores(datos):
    """
    Muestra la lista de tomadores disponibles.
    Parámetros:
        datos (list): Lista de diccionarios con los datos de tomadores.
    """
    print("\n--- Lista de Tomadores ---")
    for i, tomador in enumerate(datos):
        print(f"{i + 1}. {tomador['id_tomador']} - {tomador['nombre_tomador']}")
def generar_liquidacion(datos_recibos, datos_tomadores):
    """
    Genera una nueva liquidación basada en los recibos y siniestros.
    Parámetros:
        datos_recibos (list): Lista de diccionarios con los datos de recibos.
        datos_tomadores (list): Lista de diccionarios con los datos de tomadores.
    Retorna:
        str: Mensaje de éxito con el número de liquidación generado.
    """
    mostrar_tomadores(datos_tomadores)
    seleccion = int(input("Seleccione el número del tomador: ")) - 1
    tomador_seleccionado = datos_tomadores[seleccion]
    importe_recibos_cobrados = 0
    lista_recibos_liquidar = []
    importe_recibos_baja = 0
    lista_recibos_baja = []
    importe_siniestros_pagados = 0
    lista_siniestros_liquidados = []
    for r in datos_recibos:
        if r.get('estado_recibo') in ['Cobrado', 'Cobrado_banco'] and r.get('estado_liquidacion') == 'Pendiente':
            importe_recibos_cobrados += float(r.get('importe_pagar', 0))
            lista_recibos_liquidar.append((r['nro_poliza'], r['id_recibo']))
        if r.get('estado_recibo') == 'Baja' and r.get('estado_liquidacion') == 'Pendiente':
            importe_recibos_baja += float(r.get('importe_pagar', 0))
            lista_recibos_baja.append((r['nro_poliza'], r['id_recibo']))
        if r.get('estado_siniestro') == 'Pagado' and r.get('estado_liquidacion') == 'Pendiente':
            importe_siniestros_pagados += float(r.get('importe_pagar_siniestro', 0))
            lista_siniestros_liquidados.append((r['nro_poliza'], r['nro_siniestro']))
#Genera un nuevo número de liquidación
    nro_liquidacion = f"{datetime.now().year}-{len(datos_recibos) + 1:04d}"
#Crea una lista de datos para la nueva liquidación
    nueva_liquidacion = {
        'nro_liquidacion': nro_liquidacion,
        'fecha_liquidacion': datetime.now().strftime("%Y-%m-%d"),
        'estado_liquidacion': 'Pendiente',
        'importe_recibos_cobrados': importe_recibos_cobrados,
        'importe_recibos_baja': importe_recibos_baja,
        'importe_siniestros_pagados': importe_siniestros_pagados,
        'importe_liquidacion': (importe_recibos_cobrados - importe_siniestros_pagados, importe_recibos_baja),
        'lista_recibos_liquidar': ', '.join([f"{poliza}-{recibo}" for poliza, recibo in lista_recibos_liquidar]),
        'lista_recibos_baja': ', '.join([f"{poliza}-{recibo}" for poliza, recibo in lista_recibos_baja]),
        'lista_siniestros_liquidados': ', '.join([f"{poliza}-{siniestro}" for poliza, siniestro in lista_siniestros_liquidados]),
        'id_tomador': tomador_seleccionado['id_tomador'],
    }
#Actualiza el estado del tomador en lugar de crear una nueva entrada
    for tomador in datos_tomadores:
        if tomador['id_tomador'] == tomador_seleccionado['id_tomador']:
            tomador.update({
                'estado_liquidacion': 'Pendiente',
                'nro_liquidacion': nro_liquidacion
            })
#Agrega la nueva liquidación a los datos
    datos_recibos.append(nueva_liquidacion)
    guardar_datos(datos_recibos)
    guardar_datos(datos_tomadores)
    return f"Liquidación {nro_liquidacion} generada exitosamente para el tomador {tomador_seleccionado['nombre_tomador']}."
def cerrar_liquidacion(nro_liquidacion, datos):
    """
    Cierra una liquidación existente.
    Parámetros:
        nro_liquidacion (str): Número de la liquidación a cerrar.
        datos (list): Lista de diccionarios con los datos de liquidaciones.
    Retorna:
        str: Mensaje de éxito o error.
    """
    for liquidacion in datos:
        if liquidacion['nro_liquidacion'] == nro_liquidacion:
            liquidacion['estado_liquidacion'] = 'Liquidado'
            guardar_datos(datos)
            return f"Liquidación {nro_liquidacion} Liquidado exitosamente."
    return "Error: Liquidación no encontrada."
def modificar_liquidacion(nro_liquidacion, nuevos_datos, datos):
    """
    Modifica una liquidación existente.
    Parámetros:
        nro_liquidacion (str): Número de la liquidación a modificar.
        nuevos_datos (dict): Diccionario con los nuevos datos de la liquidación.
        datos (list): Lista de diccionarios con los datos de liquidaciones.
    Retorna:
        str: Mensaje de éxito o error.
    """
    for liquidacion in datos:
        if liquidacion['nro_liquidacion'] == nro_liquidacion:
            liquidacion.update(nuevos_datos)
            guardar_datos(datos)
            return f"Liquidación {nro_liquidacion} modificada exitosamente."
    return "Error: Liquidación no encontrada."
def menu():
    """
    Muestra el menú de liquidaciones y gestiona las opciones seleccionadas.
    """
    datos_recibos = cargar_datos()
#Carga los datos de tomadores desde el mismo CSV
    datos_tomadores = cargar_datos()  
    while True:
        print("\n--- Menú de Liquidaciones ---")
        print("1. Generar Liquidación")
        print("2. Cerrar Liquidación")
        print("3. Modificar Liquidación")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            print(generar_liquidacion(datos_recibos, datos_tomadores))
        elif opcion == "2":
            nro_liquidacion = input("Ingrese el número de liquidación a cerrar: ")
            print(cerrar_liquidacion(nro_liquidacion, datos_recibos))
        elif opcion == "3":
            nro_liquidacion = input("Ingrese el número de liquidación a modificar: ")
            nuevos_datos = {}
            nuevos_datos['estado_liquidacion'] = input("Ingrese el nuevo estado de la liquidación (Pendiente/Liquidado): ")
            print(modificar_liquidacion(nro_liquidacion, nuevos_datos, datos_recibos))
        elif opcion == "9":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()