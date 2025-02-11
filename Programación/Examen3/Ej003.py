#Se tiene un archivo CSV con información de productos en un almacén. Cada fila representa un producto con los siguientescampos:
# ID: identificador único del producto
# Nombre: nombre del producto
# Categoría: Categoría del producto
# Precio Precio del producto
# stock: cantidad disponible en inventario.
# El programa, debe hacer que la función (def convertirCSV2JSON(csv_filename, json_filename, categoria_filtro):
#- Lea los datos del archivo CSV
#- Filtre solo los productos de la categoría epecificada en categoria_filtro.
#Guarde los productos filtrados en un archivo JSON, donde cada producto debe representarse como un diccionario.
#Nombre de ficheros son: entrada.csv y salida.json
import csv
import json
import os
def convertirCSV2JSON(csv_filename, json_filename, categoria_filtro):
    productos_filtrados = []
    try:
        ARCHRUTAS = os.path.dirname(os.path.abspath(__file__))
        csv_ruta = os.path.join(ARCHRUTAS, csv_filename)
        json_ruta = os.path.join(ARCHRUTAS, json_filename)
#Abrimos el csv para poder hacer las comparacones a la hora de filtrar por la categoría
        with open(csv_ruta, mode='r', encoding='utf-8') as archcsv:
            lector = csv.DictReader(archcsv)
            for fila in lector:
                if fila['Categoría'] == categoria_filtro:
                    productos_filtrados.append(fila)
#Una vez leido el csv, procedemos a crear el json con los parametros solicitados.
        with open(json_ruta, mode='w', encoding='utf-8') as archjson:
            json.dump(productos_filtrados, archjson, indent=4, ensure_ascii=False)
        print(f"Archivo JSON '{json_ruta}' creado con éxito.")
    except Exception as e:
        print(f"Error: {e}")
def main():
    convertirCSV2JSON('entrada.csv', 'salida.json', 'Electrónica')

if __name__ == "__main__":
    main()