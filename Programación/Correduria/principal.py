
"""
Módulo principal que gestiona el menú de la aplicación.
"""
from Polizas import menu_polizas
from Tomadores import menu_tomadores
from Recibos import menu_recibos
from Siniestros import menu_siniestros
from Liquidaciones import menu_liquidaciones
from Estadisticas import menu_estadisticas

def main():
    while True:
        print("""
        Correduría Mi Coche Asegurado

        Menú principal:
        1. Pólizas
        2. Tomadores
        3. Recibos
        4. Siniestros
        5. Liquidaciones
        6. Estadística
        9. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            menu_polizas()
        elif opcion == '2':
            menu_tomadores()
        elif opcion == '3':
            menu_recibos()
        elif opcion == '4':
            menu_siniestros()
        elif opcion == '5':
            menu_liquidaciones()
        elif opcion == '6':
            menu_estadisticas()
        elif opcion == '9':
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()