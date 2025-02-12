"""
Autores: Víctor Fernandez Díaz ~ Marcos Javier Pérez Gómez
"""
import Polizas
import Tomadores
import Recibos
import Siniestros
import Liquidaciones
import Estadisticas

def main():
    """Muestra el menú principal y gestiona las opciones seleccionadas."""
    while True:
        print("""
        Correduría Mi Coche Asegurado:
        1. Pólizas
        2. Tomadores
        3. Recibos
        4. Siniestros
        5. Liquidaciones
        6. Estadística
        0. Salir del programa
        """)
        opcion = input("Seleccione una opción: ")
#Llamada al módulo correspondiente según la opción elegida
        if opcion == '1':
            Polizas.menu()
        elif opcion == '2':
            Tomadores.menu()
        elif opcion == '3':
            Recibos.menu()
        elif opcion == '4':
            Siniestros.menu()
        elif opcion == '5':
            Liquidaciones.menu()
        elif opcion == '6':
            Estadisticas.menu()
        elif opcion == '0':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 

if __name__ == "__main__":
    main()