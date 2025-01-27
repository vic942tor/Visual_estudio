
"""
Funciones para gestionar tomadores.
Autores: [Nombre1, Nombre2]
"""
def menu_tomadores():
    while True:
        print("""
        Menú Tomadores:
        1. Crear Tomador
        2. Modificar Tomador
        3. Eliminar Tomador
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Crear Tomador")
            # Llamar a función crear_tomador()
        elif opcion == '2':
            print("Modificar Tomador")
            # Llamar a función modificar_tomador()
        elif opcion == '3':
            print("Eliminar Tomador")
            # Llamar a función eliminar_tomador()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")