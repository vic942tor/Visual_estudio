import os
import csv
import Utilidades

# Define la ruta del archivo csv
directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")

tomadores = []

def cargar_tomadores():
    """Cargar los tomadores desde el archivo CSV."""
    global tomadores
    tomadores = []
    if os.path.exists(archivo_csv):
        with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
            lector_csv = csv.DictReader(file)
            for fila in lector_csv:
                tomadores.append(fila)
    else:
        print("Error: El archivo de tomadores no existe.")

def guardar_tomadores():
    """Guarda la lista de tomadores en el archivo CSV."""
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=tomadores[0].keys() if tomadores else [])
        writer.writeheader()
        writer.writerows(tomadores)

def agregar_tomador(id_tomador, nombre_tomador, fecha_nacimiento='', domicilio='', movil_contacto='', email_contacto=''):
    """
    Agrega un nuevo tomador a la lista de tomadores y lo guarda en el archivo CSV.
    """
    if Utilidades.validar_nif_nie_cif(id_tomador):
        tomador = {
            'id_tomador': id_tomador,
            'nombre_tomador': nombre_tomador,
            'fecha_nacimiento': fecha_nacimiento,
            'domicilio': domicilio,
            'movil_contacto': movil_contacto,
            'email_contacto': email_contacto
        }
        tomadores.append(tomador)
        guardar_tomadores()  # Guarda al csv
    else:
        print("ID de tomador no válido.")

def modificar_tomador(id_tomador, nombre_tomador=None, fecha_nacimiento=None, domicilio=None, movil_contacto=None, email_contacto=None):
    """
    Modifica los datos de un tomador existente.
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
            guardar_tomadores()  # Guarda al csv
            return
    print("Tomador no encontrado.")

def eliminar_tomador(id_tomador):
    """
    Elimina un tomador de la lista de tomadores.
    """
    global tomadores
    tomadores = [t for t in tomadores if t['id_tomador'] != id_tomador]
    guardar_tomadores()  # Guarda al csv

def listar_tomadores():
    """
    Lista todos los tomadores registrados.
    """
    if not tomadores:
        print("No hay tomadores registrados.")
        return

    print("\nLista de Tomadores:")
    print(f"{'ID Tomador':<15} {'Denominación':<30} {'Fecha Nacimiento':<15} {'Edad':<5} {'Domicilio':<40} {'Móvil':<15} {'Email':<30}")
    print("=" * 130)

    # Muestra a los tomadores en una linea ordenada
    for tomador in tomadores:
        edad = Utilidades.calcular_edad(tomador['fecha_nacimiento'])  # Calcular la edad
        print(f"{tomador['id_tomador']:<15} {tomador['nombre_tomador']:<30} {tomador['fecha_nacimiento']:<15} {edad:<5} {tomador['domicilio']:<40} {tomador['movil_contacto']:<15} {tomador['email_contacto']:<30}")

    print("=" * 130)

def menu():
    """
    Muestra el menú de opciones para gestionar tomadores.
    """
    cargar_tomadores()
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
            fecha_nacimiento = input("Ingrese fecha de nacimiento: ")
            domicilio = input("Ingrese domicilio: ")
            movil_contacto = input("Ingrese número de contacto: ")
            email_contacto = input("Ingrese dirección de correo: ")
            agregar_tomador(id_tomador, nombre_tomador, fecha_nacimiento, domicilio, movil_contacto, email_contacto)
        
        elif opcion == '2':
            id_tomador = input("Ingrese ID del tomador a modificar: ")
            nombre_tomador = input("Ingrese nuevo nombre del tomador (dejar vacío para no modificar): ") or None
            fecha_nacimiento = input("Ingrese nueva fecha de nacimiento (dejar vacío para no modificar): ") or None
            domicilio = input("Ingrese nuevo domicilio (dejar vacío para no modificar): ") or None
            movil_contacto = input("Ingrese nuevo número de contacto (dejar vacío para no modificar): ") or None
            email_contacto = input("Ingrese nueva dirección de correo (dejar vacío para no modificar): ") or None
            modificar_tomador(id_tomador, nombre_tomador, fecha_nacimiento, domicilio, movil_contacto, email_contacto)
        
        elif opcion == '3':
            id_tomador = input("Ingrese ID del tomador a eliminar: ")
            eliminar_tomador(id_tomador)
        
        elif opcion == '4':
            listar_tomadores()
        
        elif opcion == '0':
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()