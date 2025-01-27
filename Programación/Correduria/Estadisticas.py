# Estadisticas.py

def mostrar_informacion_poliza(polizas, siniestros, recibos, nro_poliza):
    """
    Muestra toda la información de una póliza específica, incluidos sus siniestros y recibos.

    Parámetros:
    - polizas (list): Lista de pólizas existentes.
    - siniestros (list): Lista de siniestros existentes.
    - recibos (list): Lista de recibos existentes.
    - nro_poliza (str): Número de la póliza a buscar.

    Retorna:
    - dict/str: Diccionario con toda la información de la póliza o mensaje de error si no existe.
    """
    # Buscar la póliza
    for poliza in polizas:
        if poliza['nro_poliza'] == nro_poliza:
            # Obtener los siniestros asociados
            siniestros_asociados = [s for s in siniestros if s['nro_poliza'] == nro_poliza]
            # Obtener los recibos asociados
            recibos_asociados = [r for r in recibos if r['nro_poliza'] == nro_poliza]
            # Retornar toda la información
            return {
                "Póliza": poliza,
                "Siniestros": siniestros_asociados,
                "Recibos": recibos_asociados,
            }

    return "Error: No se encontró la póliza especificada."

def mostrar_informacion_liquidacion(liquidaciones, nro_liquidacion):
    """
    Muestra toda la información de una liquidación específica.

    Parámetros:
    - liquidaciones (list): Lista de liquidaciones existentes.
    - nro_liquidacion (str): Número de la liquidación a buscar.

    Retorna:
    - dict/str: Diccionario con toda la información de la liquidación o mensaje de error si no existe.
    """
    # Buscar la liquidación
    for liquidacion in liquidaciones:
        if liquidacion['nro_liquidacion'] == nro_liquidacion:
            return liquidacion

    return "Error: No se encontró la liquidación especificada."

def menu_estadisticas(polizas, siniestros, recibos, liquidaciones):
    """
    Menú principal para mostrar estadísticas.

    Parámetros:
    - polizas (list): Lista de pólizas existentes.
    - siniestros (list): Lista de siniestros existentes.
    - recibos (list): Lista de recibos existentes.
    - liquidaciones (list): Lista de liquidaciones existentes.

    No retorna nada, solo imprime resultados en pantalla.
    """
    while True:
        print("\n--- Menú de Estadísticas ---")
        print("1. Mostrar información de una póliza")
        print("2. Mostrar información de una liquidación")
        print("9. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nro_poliza = input("Ingrese el número de la póliza: ")
            resultado = mostrar_informacion_poliza(polizas, siniestros, recibos, nro_poliza)
            if isinstance(resultado, dict):
                print("\nInformación de la póliza:")
                print("Póliza:", resultado["Póliza"])
                print("Siniestros:", resultado["Siniestros"])
                print("Recibos:", resultado["Recibos"])
            else:
                print(resultado)

        elif opcion == "2":
            nro_liquidacion = input("Ingrese el número de la liquidación: ")
            resultado = mostrar_informacion_liquidacion(liquidaciones, nro_liquidacion)
            if isinstance(resultado, dict):
                print("\nInformación de la liquidación:")
                for clave, valor in resultado.items():
                    print(f"{clave}: {valor}")
            else:
                print(resultado)

        elif opcion == "9":
            break

        else:
            print("Opción no válida.")
