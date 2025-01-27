
"""
Funciones para gestionar recibos.
Autores: [Nombre1, Nombre2]
"""
def menu_recibos():
    while True:
        print("""
        Menú Recibos:
        1. Crear Recibo
        2. Modificar Recibo
        3. Eliminar Recibo
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Crear Recibo")
            # Llamar a función crear_recibo()
        elif opcion == '2':
            print("Modificar Recibo")
            # Llamar a función modificar_recibo()
        elif opcion == '3':
            print("Eliminar Recibo")
            # Llamar a función eliminar_recibo()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")