# Se quiere diseñar un programa en python que permita crear un progama de autentificación de usuarios en el que se use como persistencia de los datos la librería pickle.
# La estructura de datos que se debe utilizar, es un diccionario donde la clave será el NIF y el valor una lista con el resto de valores que se deben guardar del usuario
# El resto de datos a almacenar son:
# Nombre de usuario: string de 8 caracteres
# Nombre comppleto: Nombre y apellido de la persona
# Edad: un número entero que debe ser >= a 18 y < a 70
# Estado civil: un string con valores dentro del siguiente rango (casado,divorciado,viudo,soltero)
# contraseña: 

# 1-- Entrar o Salir
# debe revisar un archivo pckl para ver si el usuario está registrado, si no pide que se cree uno nuevo
import pickle
import os   
ARCHIVO_PCKL = 'usuarios.pckl'
def leer_usuarios():
    try:
        if os.path.exists(ARCHIVO_PCKL):
            with open(ARCHIVO_PCKL, mode='rb') as archivo:
                return pickle.load(archivo)
        else:
            return {}
    except:
        print(f"Error a la hora de leer el archivo")
        return {}
def guardar_usuarios(usuarios):
    try:
        with open(ARCHIVO_PCKL, mode='wb') as archivo:
            pickle.dump(usuarios, archivo)
    except:
        print(f"Error a la hora de guardar los datos")
def main():
    usuarios = leer_usuarios()
    while True:
        print('1. Entrar')
        print('2. Salir')
        respuesta = input('Seleccione qué desea hacer: ')
        if respuesta == '2':
            break
        elif respuesta == '1':
            while True:
                print('1. acceder mediante usuario')
                print('2. acceder mediante NIF')
                respuesta2 = input('Seleccione una de las opciones: ')
                if respuesta2 == '2':
                    nif = input('Ingrese su NIF: ')
                    if nif in usuarios:
                        print(f"Bienvenido {usuarios[nif][0]}")
                    else:
                        try:
                            print("Usuario no encontrado. Debe registrarse.")
                            nombre_usuario = input('Nombre de usuario (8 caracteres): ')
                            nombre_completo = input('Nombre completo: ')
                            edad = int(input('Edad (18-69): '))
                            estado_civil = input('Estado civil (casad@, divorciad@, viud@, solter@): ')
                            contrasena = input('Contraseña (6-10 caracteres, letras y números, al menos una mayúscula y minúscula): ')
                            if 18 <= edad < 70 and estado_civil not in ('casado', 'divorciado', 'viudo', 'soltero','casada', 'divorciada', 'viuda', 'soltera'):
                                guardar_usuarios(usuarios)
                            elif len(nombre_usuario) < 8 or len(nombre_usuario) > 8:
                                guardar_usuarios(usuarios)
                            elif nombre_completo != '':
                                guardar_usuarios(usuarios)
                                for i in range(len(contrasena)):
                                    if not contrasena[i].isalnum() or contrasena[i].islower() or contrasena[i].isupper() or contrasena[i].isdigit() or contrasena[0].isdigit():
                                        print("Contraseña inválida. Intente nuevamente.")
                                        break
                            usuarios[nif] = [nombre_usuario, nombre_completo, edad, estado_civil, contrasena]
                            guardar_usuarios(usuarios)
                            print("Usuario registrado correctamente.")
                            break
                        except:
                            print("Error al registrar el usuario.")

if __name__ == "__main__":
    main()

                