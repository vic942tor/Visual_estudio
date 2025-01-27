
"""
Funciones para generar estadísticas.
Autores: [Nombre1, Nombre2]
"""
def menu_estadisticas():
    while True:
        print("""
        Menú Estadísticas:
        1. Ver Estadísticas de Póliza
        2. Ver Estadísticas de Liquidaciones
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Estadísticas de Póliza")
            # Llamar a función estadisticas_poliza()
        elif opcion == '2':
            print("Ver Estadísticas de Liquidaciones")
            # Llamar a función estadisticas_liquidaciones()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")