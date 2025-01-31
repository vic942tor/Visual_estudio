import pickle
from Polizas import menu_polizas
# from Tomadores import menu_tomadores
# from Recibos import menu_recibos
# from Siniestros import menu_siniestros
from Liquidaciones import menu_liquidaciones
from Estadisticas import menu_estadisticas

# Archivo para cargar los datos
FICHERO_DATOS = "correduria_data.pkl"

# Cargar datos desde el archivo pickle o inicializar datos vacíos
def cargar_datos():
    """
    Carga los datos desde el archivo pickle o inicializa datos vacíos.

    Returns:
        dict: Diccionario con los datos cargados.
    """
    try:
        with open(FICHERO_DATOS, "rb") as file:
            return pickle.load(file)
    except:
        return {
            "polizas": [],
            "tomadores": [],
            "recibos": [],
            "siniestros": [],
            "liquidaciones": []
        }

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
            menu_polizas(
                datos["polizas"], 
                datos["tomadores"], 
                datos["siniestros"], 
                datos["recibos"],
            )
        # elif opcion == '2':
        #     menu_tomadores(
        #         datos["tomadores"], 
        #         datos["polizas"]
        #     )
        # elif opcion == '3':
        #     menu_recibos(
        #         datos["recibos"], 
        #         datos["polizas"]
        #     )
        # elif opcion == '4':
        #     menu_siniestros(
        #         datos["siniestros"], 
        #         datos["polizas"]
        #     )
        elif opcion == '5':
            menu_liquidaciones(
                datos["recibos"], 
                datos["siniestros"], 
                datos["liquidaciones"]
            )
        elif opcion == '6':
            menu_estadisticas(
                datos["polizas"], 
                datos["liquidaciones"]
            )
        elif opcion == '9':
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
