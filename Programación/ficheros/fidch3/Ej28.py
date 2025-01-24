# Una empresa trabajo con Nombre, NIF, Municipio tenemos una sede en tenerie con un fichero tenerife.csv y grancanaria.csv
# una linea es TNF sin encabezado (Pepe;12345678X;Los Rodeos) GC con encabezado:
# ( Nombre;NIF;municipio
#   Joaquin;87654321X;Telde)
#Se pide crear un programa que lea los ficheros y genere un archivo llamado trabajannombre.json con el nombre de los trabajadores que hayan trabajado tanto en tenerife como en grancanaria (tenerife.csv y grancanaria.csv)

import csv
import json
def leer_trabajadores_tenerife(archivo):
    trabajadores_tenerife = set()
    with open(archivo, 'r') as f:
        for linea in f:
            nombre, _, _ = linea.strip().split(';')
            trabajadores_tenerife.add(nombre)
    return trabajadores_tenerife

def leer_trabajadores_grancanaria(archivo):
    trabajadores_grancanaria = set()
    with open(archivo, 'r') as f:
        lector = csv.DictReader(f, delimiter=';')
        for fila in lector:
            trabajadores_grancanaria.add(fila['Nombre'])
    return trabajadores_grancanaria

def main():
    archivo_tenerife = 'tenerife.csv'
    archivo_grancanaria = 'grancanaria.csv'
    archivo_salida = 'trabajannombre.json'
    
    # Leer trabajadores de ambos archivos
    trabajadores_tenerife = leer_trabajadores_tenerife(archivo_tenerife)
    trabajadores_grancanaria = leer_trabajadores_grancanaria(archivo_grancanaria)
    
    # Obtener intersección
    trabajadores_comunes = list(trabajadores_tenerife & trabajadores_grancanaria)
    
    # Guardar en archivo JSON
    with open(archivo_salida, 'w') as f:
        json.dump(trabajadores_comunes, f, indent=4)
    
    print(f"Se ha creado el archivo {archivo_salida} con los nombres de los trabajadores comunes.")

if __name__ == "__main__":
    main()



