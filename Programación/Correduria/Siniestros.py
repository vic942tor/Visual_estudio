
"""
Funciones para gestionar siniestros.
Autores: [Nombre1, Nombre2]
"""
def menu_siniestros():
    while True:
        print("""
        Menú Siniestros:
        1. Crear Siniestro
        2. Modificar Siniestro
        3. Eliminar Siniestro
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Crear Siniestro")
            # Llamar a función crear_siniestro()
        elif opcion == '2':
            print("Modificar Siniestro")
            # Llamar a función modificar_siniestro()
        elif opcion == '3':
            print("Eliminar Siniestro")
            # Llamar a función eliminar_siniestro()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")