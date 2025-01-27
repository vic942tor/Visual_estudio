# Una empresa trabajo con Nombre, NIF, Municipio tenemos una sede en tenerie con un fichero tenerife.csv y grancanaria.csv
# una linea es TNF sin encabezado (Pepe;12345678X;Los Rodeos) GC con encabezado:
# ( Nombre;NIF;municipio
#   Joaquin;87654321X;Telde)
#Se pide crear un programa que lea los ficheros y genere un archivo llamado trabajannombre.json con el nombre de los trabajadores que hayan trabajado tanto en tenerife como en grancanaria (tenerife.csv y grancanaria.csv)

import csv
import json

def leer_fichero(fichero):
    with open(fichero, 'r') as file:
        reader = csv.reader(file)







