import Polizas
import Tomadores
import Recibos
import Siniestros
import Liquidaciones
import Estadisticas

def main():
    """Muestra el menú principal y gestiona las opciones seleccionadas."""
    while True:
        print("\nCorreduría Mi Coche Asegurado")
        print("1. Pólizas")
        print("2. Tomadores")
        print("3. Recibos")
        print("4. Siniestros")
        print("5. Liquidaciones")
        print("6. Estadística")
        print("9. Salir")
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
        elif opcion == '9':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 

if __name__ == "__main__":
    main()


