import csv
import os
from datetime import datetime

directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")
def cargar_datos():
    datos = []
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as f:
            lector_csv = csv.DictReader(f)
            datos = list(lector_csv)
    except FileNotFoundError:
        print("Error: Archivo de datos no encontrado.")
    return datos
def guardar_datos(datos):
    if datos:
        with open(archivo_csv, "w", newline='', encoding='utf-8') as f:
            fieldnames = datos[0].keys()
            escribir_csv = csv.DictWriter(f, fieldnames=fieldnames)
            escribir_csv.writeheader()
            escribir_csv.writerows(datos)
def mostrar_usuarios(datos):
    usuarios = set(r['id_tomador'] for r in datos if 'id_tomador' in r and r.get('estado_recibo'))
    if not usuarios:
        print("No hay usuarios con recibos disponibles.")
        return None
    print("\nUsuarios con recibos disponibles:")
    for usuario in usuarios:
        print(usuario)
    return usuarios
def generar_liquidacion(datos):
    usuarios_disponibles = mostrar_usuarios(datos)
    if not usuarios_disponibles:
        return "No hay usuarios con recibos disponibles para liquidación."
    id_tomador = input("Ingrese el ID del tomador para la liquidación: ")
    if id_tomador not in usuarios_disponibles:
        return "Error: ID de tomador no válido."
    importe_recibos_cobrados = 0
    importe_siniestros_pagados = 0
    importe_recibos_baja = 0
    for r in datos:
        if r.get('id_tomador') == id_tomador:
            if r.get('estado_recibo') in ['Cobrado', 'Cobrado_banco'] and r.get('estado_liquidacion') == 'Pendiente':
                importe_recibos_cobrados += float(r.get('importe_pagar', 0))
            if r.get('estado_siniestro') == 'Pagado' and r.get('estado_liquidacion') == 'Pendiente':
                importe_siniestros_pagados += float(r.get('importe_pagar_siniestro', 0))
            if r.get('estado_recibo') == 'Baja' and r.get('estado_liquidacion') == 'Pendiente':
                importe_recibos_baja += float(r.get('importe_pagar', 0))
    
    total_liquidacion = importe_recibos_cobrados - importe_siniestros_pagados - importe_recibos_baja
    nro_liquidacion = f"{datetime.now().year}-{len(datos) + 1:04d}"
    for r in datos:
        if r.get('id_tomador') == id_tomador:
            r.update({
                'nro_liquidacion': nro_liquidacion,
                'fecha_liquidacion': datetime.now().strftime("%Y-%m-%d"),
                'estado_liquidacion': 'Pendiente',
                'importe_recibos_cobrados': importe_recibos_cobrados,
                'importe_siniestros_pagados': importe_siniestros_pagados,
                'importe_recibos_baja': importe_recibos_baja,
                'importe_liquidacion': total_liquidacion
            })
            break
    
    guardar_datos(datos)
    return f"Liquidación {nro_liquidacion} actualizada exitosamente para el tomador {id_tomador}."
def cerrar_liquidacion(nro_liquidacion, datos):
    for liquidacion in datos:
        if liquidacion['nro_liquidacion'] == nro_liquidacion:
            liquidacion['estado_liquidacion'] = 'Liquidado'
            guardar_datos(datos)
            return f"Liquidación {nro_liquidacion} cerrada exitosamente."
    return "Error: Liquidación no encontrada."
def menu():
    datos = cargar_datos()
    while True:
        print("\n--- Menú de Liquidaciones ---")
        print("1. Generar Liquidación")
        print("2. Cerrar Liquidación")
        print("9. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            print(generar_liquidacion(datos))
        elif opcion == "2":
            nro_liquidacion = input("Ingrese el número de liquidación a cerrar: ")
            print(cerrar_liquidacion(nro_liquidacion, datos))
        elif opcion == "9":
            break
        else:
            print("Opción no válida.")
if __name__ == "__main__":
    menu()

