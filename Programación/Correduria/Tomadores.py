# Tomadores.py
# Integrantes: [Nombre del Integrante 1], [Nombre del Integrante 2]
# Este archivo contiene todas las funciones asociadas con el trabajo de los tomadores.

# Estructura de datos para los tomadores
# Tomadores: lista de diccionarios con los siguientes campos:
# - id_tomador: identificador del tomador (NIF, NIE, CIF)
# - nombre_tomador: nombre de la persona o empresa
# - fecha_nacimiento: fecha de nacimiento (opcional)
# - domicilio: domicilio del tomador
# - movil_contacto: número de contacto
# - email_contacto: dirección de correo de contacto

tomadores = []

def validar_id_tomador(id_tomador):
    if len(id_tomador) == 9 and id_tomador[:-1].isdigit() and id_tomador[-1].isalpha():
        return True
    return False

def agregar_tomador(id_tomador, nombre_tomador, fecha_nacimiento, domicilio, movil_contacto, email_contacto):
    """
    Agrega un nuevo tomador a la lista de tomadores.
    
    :param id_tomador: str - Identificador del tomador
    :param nombre_tomador: str - Nombre del tomador
    :param fecha_nacimiento: str - Fecha de nacimiento del tomador
    :param domicilio: str - Domicilio del tomador
    :param movil_contacto: str - Número de contacto
    :param email_contacto: str - Dirección de correo de contacto
    :return: None
    """
    if validar_id_tomador(id_tomador):
        tomador = {
            'id_tomador': id_tomador,
            'nombre_tomador': nombre_tomador,
            'fecha_nacimiento': fecha_nacimiento,
            'domicilio': domicilio,
            'movil_contacto': movil_contacto,
            'email_contacto': email_contacto
        }
        tomadores.append(tomador)
    else:
        print("ID de tomador no válido.")

def modificar_tomador(id_tomador, nombre_tomador=None, fecha_nacimiento=None, domicilio=None, movil_contacto=None, email_contacto=None):
    """
    Modifica los datos de un tomador existente.
    
    :param id_tomador: str - Identificador del tomador
    :param nombre_tomador: str - Nuevo nombre del tomador
    :param fecha_nacimiento: str - Nueva fecha de nacimiento del tomador
    :param domicilio: str - Nuevo domicilio del tomador
    :param movil_contacto: str - Nuevo número de contacto
    :param email_contacto: str - Nueva dirección de correo de contacto
    :return: None
    """
    for tomador in tomadores:
        if tomador['id_tomador'] == id_tomador:
            if nombre_tomador is not None:
                tomador['nombre_tomador'] = nombre_tomador
            if fecha_nacimiento is not None:
                tomador['fecha_nacimiento'] = fecha_nacimiento
            if domicilio is not None:
                tomador['domicilio'] = domicilio
            if movil_contacto is not None:
                tomador['movil_contacto'] = movil_contacto
            if email_contacto is not None:
                tomador['email_contacto'] = email_contacto
            return
    print("Tomador no encontrado.")

def eliminar_tomador(id_tomador):
    """
    Elimina un tomador de la lista de tomadores.
    
    :param id_tomador: str - Identificador del tomador
    :return: None
    """
    global tomadores
    tomadores = [tomador for tomador in tomadores if tomador['id_tomador'] != id_tomador]

def listar_tomadores():
    """
    Lista todos los tomadores registrados.
    
    :return: None
    """
    if not tomadores:
        print("No hay tomadores registrados.")
        return

    # Imprimir encabezados
    print("\nLista de Tomadores:")
    print(f"{'ID Tomador':<15} {'Denominación':<30} {'Fecha Nacimiento':<15} {'Domicilio':<40} {'Móvil':<15} {'Email':<30}")
    print("=" * 130)  # Línea separadora

    # Imprimir cada tomador en formato alineado
    for tomador in tomadores:
        print(f"{tomador['id_tomador']:<15} {tomador['nombre_tomador']:<30} {tomador['fecha_nacimiento']:<15} {tomador['domicilio']:<40} {tomador['movil_contacto']:<15} {tomador['email_contacto']:<30}")

    print("=" * 130)  # Línea separadora al final

def menu():
    """
    Muestra el menú de opciones para gestionar tomadores.
    
    :return: None
    """
    while True:
        print("""
            Menú Tomadores:
            1. Agregar Tomador
            2. Modificar Tomador
            3. Eliminar Tomador
            4. Listar Tomadores
            0. Regresar al Menú Principal
            """)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            id_tomador = input("Ingrese ID del tomador (NIF, NIE, CIF): ")
            nombre_tomador = input("Ingrese nombre del tomador: ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento (opcional): ")
            domicilio = input("Ingrese domicilio: ")
            movil_contacto = input("Ingrese número de contacto: ")
            email_contacto = input("Ingrese dirección de correo: ")
            agregar_tomador(id_tomador, nombre_tomador, fecha_nacimiento, domicilio, movil_contacto, email_contacto)
        
        elif opcion == '2':
            id_tomador = input("Ingrese ID del tomador a modificar: ")
            nombre_tomador = input("Ingrese nuevo nombre del tomador (dejar vacío para no modificar): ")
            fecha_nacimiento = input("Ingrese nueva fecha de nacimiento (dejar vacío para no modificar): ")
            domicilio = input("Ingrese nuevo domicilio (dejar vacío para no modificar): ")
            movil_contacto = input("Ingrese nuevo número de contacto (dejar vacío para no modificar): ")
            email_contacto = input("Ingrese nueva dirección de correo (dejar vacío para no modificar): ")
            modificar_tomador(id_tomador, nombre_tomador or None, fecha_nacimiento or None, domicilio or None, movil_contacto or None, email_contacto or None)
        
        elif opcion == '3':
            id_tomador = input("Ingrese ID del tomador a eliminar: ")
            eliminar_tomador(id_tomador)
        
        elif opcion == '4':
            listar_tomadores()
        
        elif opcion == '0':
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
