
"""
Funciones para gestionar liquidaciones.
Autores: [Nombre1, Nombre2]
"""
def menu_liquidaciones():
    while True:
        print("""
        Menú Liquidaciones:
        1. Generar Liquidación
        2. Modificar Liquidación
        3. Cerrar Liquidación
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Generar Liquidación")
            # Llamar a función generar_liquidacion()
        elif opcion == '2':
            print("Modificar Liquidación")
            # Llamar a función modificar_liquidacion()
        elif opcion == '3':
            print("Cerrar Liquidación")
            # Llamar a función cerrar_liquidacion()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")