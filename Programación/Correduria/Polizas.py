
"""
Funciones para gestionar pólizas.
Autores: [Nombre1, Nombre2]
"""
def menu_polizas():
    while True:
        print("""
        Menú Pólizas:
        1. Crear Póliza
        2. Modificar Póliza
        3. Eliminar Póliza
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Crear Póliza")
            # Llamar a función crear_poliza()
        elif opcion == '2':
            print("Modificar Póliza")
            # Llamar a función modificar_poliza()
        elif opcion == '3':
            print("Eliminar Póliza")
            # Llamar a función eliminar_poliza()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")