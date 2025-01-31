
def crear_poliza(polizas, tomadores, nueva_poliza):
    """
    Crea una nueva póliza si el tomador existe y no hay otra póliza con el mismo número.

    Parámetros:
    - polizas (list): Lista de pólizas existentes.
    - tomadores (list): Lista de tomadores existentes.
    - nueva_poliza (dict): Diccionario con los datos de la nueva póliza.

    Retorna:
    - str: Mensaje indicando el resultado de la operación.
    """
    # Validar que el número de póliza no exista
    for poliza in polizas:
        if poliza['nro_poliza'] == nueva_poliza['nro_poliza']:
            return "Error: El número de póliza ya existe."

    # Validar que el tomador exista
    tomador_existe = False
    for t in tomadores:
        if t['id_tomador'] == nueva_poliza['id_tomador']:
            tomador_existe = True
            break

    if not tomador_existe:
        return "Error: El tomador no existe."

    # Agregar la póliza
    polizas.append(nueva_poliza)
    return "Póliza creada exitosamente."

# Función para modificar una póliza existente
def modificar_poliza(polizas, nro_poliza, nuevos_datos):
    """
    Modifica los datos de una póliza existente (excepto su número).

    Parámetros:
    - polizas (list): Lista de pólizas existentes.
    - nro_poliza (str): Número de la póliza a modificar.
    - nuevos_datos (dict): Diccionario con los nuevos datos de la póliza.

    Retorna:
    - str: Mensaje indicando el resultado de la operación.
    """
    for poliza in polizas:
        if poliza['nro_poliza'] == nro_poliza:
            for clave, valor in nuevos_datos.items():
                if clave != 'nro_poliza':
                    poliza[clave] = valor
            return "Póliza modificada exitosamente."
    return "Error: No se encontró la póliza especificada."

# Función para eliminar una póliza
def eliminar_poliza(polizas, siniestros, recibos, nro_poliza):
    """
    Elimina una póliza y sus datos asociados (siniestros y recibos) si no está vigente.

    Parámetros:
    - polizas (list): Lista de pólizas existentes.
    - siniestros (list): Lista de siniestros existentes.
    - recibos (list): Lista de recibos existentes.
    - nro_poliza (str): Número de la póliza a eliminar.

    Retorna:
    - str: Mensaje indicando el resultado de la operación.
    """
    for poliza in polizas:
        if poliza['nro_poliza'] == nro_poliza:
            if poliza['estado_poliza'] != 'Baja':
                return "Error: No se puede eliminar una póliza vigente."

            # Eliminar siniestros asociados
            nuevos_siniestros = []
            for s in siniestros:
                if s['nro_poliza'] != nro_poliza:
                    nuevos_siniestros.append(s)
            
            siniestros[:] = nuevos_siniestros

            # Eliminar recibos asociados
            nuevos_recibos = []
            for r in recibos:
                if r['nro_poliza'] != nro_poliza:
                    nuevos_recibos.append(r)
            
            recibos[:] = nuevos_recibos

            # Eliminar la póliza
            polizas.remove(poliza)
            return "Póliza eliminada exitosamente."

    return "Error: No se encontró la póliza especificada."

# Función para listar todas las pólizas
def listar_polizas(polizas):
    """
    Retorna una lista con información resumida de todas las pólizas.

    Parámetros:
    - polizas (list): Lista de pólizas existentes.

    Retorna:
    - list: Lista con información de las pólizas.
    """
    resumen = []
    for p in polizas:
        resumen.append({
            'nro_poliza': p['nro_poliza'],
            'id_tomador': p['id_tomador'],
            'matricula': p['matricula'],
            'estado_poliza': p['estado_poliza']
        })
    return resumen

# Función para buscar información completa de una póliza
def buscar_poliza(polizas, nro_poliza):
    """
    Busca y retorna la información completa de una póliza.

    Parámetros:
    - polizas (list): Lista de pólizas existentes.
    - nro_poliza (str): Número de la póliza a buscar.

    Retorna:
    - dict/str: Diccionario con los datos de la póliza o un mensaje de error.
    """
    for poliza in polizas:
        if poliza['nro_poliza'] == nro_poliza:
            return poliza
    return "Error: No se encontró la póliza especificada."

# Función para el menú de pólizas
def menu_polizas(polizas, tomadores, siniestros, recibos):
    while True:
        print("\n--- Menú de Pólizas ---")
        print("1. Crear Póliza")
        print("2. Modificar Póliza")
        print("3. Eliminar Póliza")
        print("4. Listar Pólizas")
        print("5. Buscar Póliza")
        print("9. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":  # Crear póliza
            nro_poliza = input("Número de póliza: ")
            id_tomador = input("ID del tomador: ")
            matricula = input("Matrícula del vehículo: ")
            tipo = input("Tipo de vehículo (Ciclomotor/Moto/Turismo/Furgoneta/Camión): ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            funcionamiento = input("Funcionamiento (Combustión/Eléctrico/Mixto): ")
            estado = input("Estado de la póliza (Cobrada/PteCobro/Baja): ")
            forma_pago = input("Forma de pago (Efectivo o Banco,IBAN): ")

            nueva_poliza = {
                "nro_poliza": nro_poliza,
                "id_tomador": id_tomador,
                "matricula": matricula,
                "datos_vehiculo": (tipo, marca, modelo, funcionamiento),
                "estado_poliza": estado,
                "forma_pago": forma_pago.split(",") if "," in forma_pago else forma_pago,
            }

            print(crear_poliza(polizas, tomadores, nueva_poliza))

        elif opcion == "2":  # Modificar póliza
            nro_poliza = input("Número de póliza a modificar: ")
            nuevos_datos = {}
            matricula = input("Nueva matrícula del vehículo (o enter para no cambiar): ")
            if matricula:
                nuevos_datos["matricula"] = matricula
            estado = input("Nuevo estado de la póliza (o enter para no cambiar): ")
            if estado:
                nuevos_datos["estado_poliza"] = estado

            print(modificar_poliza(polizas, nro_poliza, nuevos_datos))

        elif opcion == "3":  # Eliminar póliza
            nro_poliza = input("Número de póliza a eliminar: ")
            print(eliminar_poliza(polizas, siniestros, recibos, nro_poliza))

        elif opcion == "4":  # Listar pólizas
            for p in listar_polizas(polizas):
                print(p)

        elif opcion == "5":  # Buscar póliza
            nro_poliza = input("Número de póliza a buscar: ")
            print(buscar_poliza(polizas, nro_poliza))

        elif opcion == "9":  # Salir del menú
            break

        else:
            print("Opción no válida.")


