
"""
Módulo para gestionar las liquidaciones en la aplicación.
Autores: [Nombre1, Nombre2]
"""
def generar_liquidacion(recibos, siniestros, liquidaciones):
    """
    Genera una nueva liquidación basada en los recibos y siniestros pendientes.

    Parámetros:
    - recibos (list): Lista de recibos existentes.
    - siniestros (list): Lista de siniestros existentes.
    - liquidaciones (list): Lista de liquidaciones existentes.

    Retorna:
    - str: Mensaje indicando el resultado de la operación.
    """
    # Calcular los importes y listas necesarias
    importe_recibos_cobrados = 0
    lista_recibos_liquidar = []
    for r in recibos:
        if r['estado_recibo'] in ['Cobrado', 'Cobrado_banco'] and r['estado_liquidacion'] == 'Pendiente':
            importe_recibos_cobrados += r['importe_pagar']
            lista_recibos_liquidar.append((r['nro_poliza'], r['id_recibo']))

    importe_recibos_baja = 0
    lista_recibos_baja = []
    for r in recibos:
        if r['estado_recibo'] == 'Baja' and r['estado_liquidacion'] == 'Pendiente':
            importe_recibos_baja += r['importe_pagar']
            lista_recibos_baja.append((r['nro_poliza'], r['id_recibo']))

    importe_siniestros_pagados = 0
    lista_siniestros_liquidados = []
    for s in siniestros:
        if s['estado_siniestro'] == 'Pagado' and s['estado_liquidacion'] == 'Pendiente':
            importe_siniestros_pagados += s['importe_pagar']
            lista_siniestros_liquidados.append((s['nro_poliza'], s['nro_siniestro']))

    # Crear nueva liquidación
    nro_liquidacion = f"{len(liquidaciones) + 1:04d}"
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

    # Actualizar estados de los elementos relacionados
    for r in recibos:
        if (r['nro_poliza'], r['id_recibo']) in lista_recibos_liquidar or (r['nro_poliza'], r['id_recibo']) in lista_recibos_baja:
            r['estado_liquidacion'] = 'Liquidado'

    for s in siniestros:
        if (s['nro_poliza'], s['nro_siniestro']) in lista_siniestros_liquidados:
            s['estado_liquidacion'] = 'Liquidado'

    # Agregar la liquidación a la lista
    liquidaciones.append(nueva_liquidacion)
    return f"Liquidación {nro_liquidacion} generada exitosamente."

def cerrar_liquidacion(liquidaciones, nro_liquidacion):
    """
    Cierra una liquidación cambiando su estado a 'Cerrada'.

    Parámetros:
    - liquidaciones (list): Lista de liquidaciones existentes.
    - nro_liquidacion (str): Número de la liquidación a cerrar.

    Retorna:
    - str: Mensaje indicando el resultado de la operación.
    """
    for liquidacion in liquidaciones:
        if liquidacion['nro_liquidacion'] == nro_liquidacion:
            if liquidacion['estado_liquidacion'] == 'Cerrada':
                return "Error: La liquidación ya está cerrada."
            liquidacion['estado_liquidacion'] = 'Cerrada'
            return f"Liquidación {nro_liquidacion} cerrada exitosamente."

    return "Error: No se encontró la liquidación especificada."

def listar_liquidaciones(liquidaciones):
    """
    Lista todas las liquidaciones con su información básica.

    Parámetros:
    - liquidaciones (list): Lista de liquidaciones existentes.

    Retorna:
    - list: Lista con información resumida de las liquidaciones.
    """
    return [
        {
            'nro_liquidacion': l['nro_liquidacion'],
            'fecha_liquidacion': l['fecha_liquidacion'],
            'estado_liquidacion': l['estado_liquidacion'],
            'importe_liquidacion': l['importe_liquidacion']
        }
        for l in liquidaciones
    ]

def menu_liquidaciones(recibos, siniestros, liquidaciones):
    """
    Menú para gestionar las liquidaciones.
    """
    while True:
        print("\n--- Menú de Liquidaciones ---")
        print("1. Generar Liquidación")
        print("2. Cerrar Liquidación")
        print("3. Listar Liquidaciones")
        print("9. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(generar_liquidacion(recibos, siniestros, liquidaciones))
        elif opcion == "2":
            nro_liquidacion = input("Número de liquidación a cerrar: ")
            print(cerrar_liquidacion(liquidaciones, nro_liquidacion))
        elif opcion == "3":
            for l in listar_liquidaciones(liquidaciones):
                print(l)
        elif opcion == "9":
            break
        else:
            print("Opción no válida.")