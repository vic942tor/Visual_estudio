# Siniestros.py

def menu_siniestros(datos):
    """
    Muestra el menú de opciones para gestionar los siniestros.
    Permite crear, modificar o eliminar siniestros.
    """
    opciones = {
        '1': crear_siniestro,
        '2': modificar_siniestro,
        '3': eliminar_siniestro,
        '9': lambda: None  # Regresar al menú principal
    }

    while True:
        print("""
        Menú Siniestros:
        1. Crear Siniestro
        2. Modificar Siniestro
        3. Eliminar Siniestro
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")

        if opcion in opciones:
            if opcion == '9':
                break
            opciones[opcion](datos)  # Llamamos la función correspondiente pasando los datos
        else:
            print("Opción no válida.")

def crear_siniestro(datos):
    """
    Crea un nuevo siniestro y lo agrega a la lista de siniestros.
    """
    nro_siniestro = input("Ingrese el número de siniestro (formato aaaanro_correlativo): ")
    
    # Verificar que el siniestro no exista
    if any(s['nro_siniestro'] == nro_siniestro for s in datos['siniestros']):
        print("El siniestro con este número ya existe.")
        return

    nro_poliza = input("Ingrese el número de la póliza asociada: ")
    
    # Verificar que la póliza exista
    if not any(p['nro_poliza'] == nro_poliza for p in datos['polizas']):
        print("La póliza con ese número no existe.")
        return

    descripcion = input("Ingrese una descripción del siniestro: ")
    matricula_contrario = input("Ingrese la matrícula del vehículo contrario: ")
    compania_contrario = input("Ingrese la compañía aseguradora del contrario: ")
    nro_poliza_contrario = input("Ingrese el número de la póliza del contrario: ")

    # Completamos el nuevo siniestro
    siniestro = {
        'nro_siniestro': nro_siniestro,
        'nro_poliza': nro_poliza,
        'descripcion': descripcion,
        'matricula_contrario': matricula_contrario,
        'compania_contrario': compania_contrario,
        'nro_poliza_contrario': nro_poliza_contrario,
        'importe_pagar': 0.0,  # Inicializamos el importe por pagar
        'estado_siniestro': 'PendienteConfirmar',
        'fecha_abono': None,
        'estado_liquidacion': 'Pendiente',
        'fecha_liquidacion': None
    }

    # Agregar el siniestro a la lista de siniestros
    datos['siniestros'].append(siniestro)
    print(f"Siniestro {nro_siniestro} creado correctamente.")

def modificar_siniestro(datos):
    """
    Permite modificar los detalles de un siniestro ya existente.
    """
    nro_siniestro = input("Ingrese el número de siniestro a modificar: ")
    
    siniestro = next((s for s in datos['siniestros'] if s['nro_siniestro'] == nro_siniestro), None)
    
    if not siniestro:
        print("No se encontró el siniestro.")
        return

    print(f"Detalles del siniestro {nro_siniestro}:")
    print(f"Descripción: {siniestro['descripcion']}")
    print(f"Estado: {siniestro['estado_siniestro']}")
    print("Puede modificar los siguientes campos o dejar en blanco para mantener el valor actual.")

    # Modificar los campos
    nueva_descripcion = input(f"Descripción (actual: {siniestro['descripcion']}): ")
    if nueva_descripcion:
        siniestro['descripcion'] = nueva_descripcion

    nuevo_estado = input(f"Estado (actual: {siniestro['estado_siniestro']}): ")
    if nuevo_estado:
        siniestro['estado_siniestro'] = nuevo_estado

    print(f"Siniestro {nro_siniestro} modificado correctamente.")

def eliminar_siniestro(datos):
    """
    Permite eliminar un siniestro de la lista de siniestros.
    """
    nro_siniestro = input("Ingrese el número de siniestro a eliminar: ")

    siniestro = next((s for s in datos['siniestros'] if s['nro_siniestro'] == nro_siniestro), None)

    if not siniestro:
        print("No se encontró el siniestro.")
        return

    # Verificar que no esté en estado de baja
    if siniestro['estado_siniestro'] == 'Baja':
        print("El siniestro ya está dado de baja.")
        return

    # Eliminar el siniestro
    datos['siniestros'].remove(siniestro)
    print(f"Siniestro {nro_siniestro} eliminado correctamente.")

