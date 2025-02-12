import csv
import os
from Polizas import menu_polizas
# from Tomadores import menu_tomadores
from Recibos import menu_recibos
# from Siniestros import menu_siniestros
from Liquidaciones import menu_liquidaciones
from Estadisticas import menu_estadisticas

directorio_base = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_base, "correduriadata.csv")

# Cargar datos desde un solo archivo CSV
def cargar_datos():
    """
    Carga los datos desde un único archivo CSV o inicializa una lista vacía si no existe.
    Returns:
        list: Lista de diccionarios con los datos cargados.
    """
    datos = []
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            datos = list(reader)
    except FileNotFoundError:
        pass
    return datos

# Función para guardar datos en un solo archivo CSV
def guardar_datos(datos):
    """
    Guarda los datos en un único archivo CSV.
    Args:
        datos (list): Lista de diccionarios con los datos a guardar.
    """
    if datos:
        with open(archivo_csv, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)

def main():
    datos = cargar_datos()
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
            menu_polizas(datos)
        # elif opcion == '2':
        #     menu_tomadores(datos)
        elif opcion == '3':
            menu_recibos(datos)
        # elif opcion == '4':
        #     menu_siniestros(datos)
        elif opcion == '5':
            menu_liquidaciones(datos)
        elif opcion == '6':
            menu_estadisticas(datos)
        elif opcion == '9':
            print("Guardando datos y saliendo...")
            guardar_datos(datos)
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()


