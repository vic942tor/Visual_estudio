# Se quiere diseñar un programa en python que permita crear un progama de autentificación de usuarios en el que se use como persistencia de los datos la librería pickle.
# La estructura de datos que se debe utilizar, es un diccionario donde la clave será el NIF y el valor una lista con el resto de valores que se deben guardar del usuario
# El resto de datos a almacenar son:
# Nombre de usuario: string de 8 caracteres
# Nombre comppleto: Nombre y apellido de la persona
# Edad: un número entero que debe ser >= a 18 y < a 70
# Estado civil: un string con valores dentro del siguiente rango (casad@,divorciad@,viud@,solter@)
# contraseña: un string de longitud entre 6 y 10 caracteres que debe tener letras y números que no puede empezar por número y debe contener letras mayusculas y minusculas
# 1-- Entrar o Salir
import pickle
import os   
def leer_usuarios():
    try:
        with open(ARCHIVO_PCKL, mode='r') as archcsv:
            lector = pickle.DictReader(archcsv)
            return list(lector)
    except:
        print(f"Error a la hora de leer el archivo")

while True:
    print('1. Entrar')
    print('2. Salir')
    respuesta = input('Seleccione, que desea hacer: ')
    if respuesta == '1':
        while True:
            print('0. Salir')
            print('1. NIF')
            print('2. Nombre de usuario')
            respuesta2 = input('Que desea seleccionar: ')
            if respuesta2 == '0':
                break