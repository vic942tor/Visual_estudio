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
def generar_liquidacion(datos):
    importe_recibos_cobrados = 0
    lista_recibos_liquidar = []
    importe_recibos_baja = 0
    lista_recibos_baja = []
    importe_siniestros_pagados = 0
    lista_siniestros_liquidados = []
    for r in datos:
        if r['estado_recibo'] in ['Cobrado', 'Cobrado_banco'] and r['estado_liquidacion'] == 'Pendiente':
            importe_recibos_cobrados += float(r['importe_pagar'])
            lista_recibos_liquidar.append((r['nro_poliza'], r['id_recibo']))
        if r['estado_recibo'] == 'Baja' and r['estado_liquidacion'] == 'Pendiente':
            importe_recibos_baja += float(r['importe_pagar'])
            lista_recibos_baja.append((r['nro_poliza'], r['id_recibo']))
        if r['estado_siniestro'] == 'Pagado' and r['estado_liquidacion'] == 'Pendiente':
            importe_siniestros_pagados += float(r['importe_pagar_siniestro'])
            lista_siniestros_liquidados.append((r['nro_poliza'], r['nro_siniestro']))
    nro_liquidacion = f"{len(datos) + 1:04d}"
    nueva_liquidacion = {
        'nro_liquidacion': nro_liquidacion,
        'fecha_liquidacion': None,
        'estado_liquidacion': 'Abierta',
        'importe_recibos_cobrados': importe_recibos_cobrados,
        'lista_recibos_liquidar': lista_recibos_liquidar,
        'importe_recibos_baja': importe_recibos_baja,
        'lista_recibos_baja': lista_recibos_baja,
        'importe_siniestros_pagados': importe_siniestros_pagados,
        'lista_siniestros_liquidados': lista_siniestros_liquidados,
        'importe_liquidacion': (importe_recibos_cobrados - importe_siniestros_pagados, importe_recibos_baja)
    }
    datos.append(nueva_liquidacion)
    guardar_datos(datos)
    return f"Liquidación {nro_liquidacion} generada exitosamente."
def menu_liquidaciones():
    datos = cargar_datos()
    while True:
        print("\n--- Menú de Liquidaciones ---")
        print("1. Generar Liquidación")
        print("9. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            print(generar_liquidacion(datos))
        elif opcion == "9":
            break
        else:
            print("Opción no válida.")
