# Sabemos la importancia de las contraseñas seguras que permiten que sea difícil
# poder romperlas.
# En este ejercicio se pide un programa en Python que genere contraseñas seguras
# de forma aleatoria según el procedimiento que se describe a continuación.
# La contraseña debe tener un mínimo de 12 caracteres y un máximo de 15. Los
# caracteres que pueden formar parte de la contraseña son los siguientes:
# • Letras minúsculas desde la a hasta la z
# • Letras mayúsculas desde la A hasta Z
# • Los dígitos desde el 0 al 9.
# • Los caracteres especiales siguientes: @ # % $ & ? ¿ ¡ ! *

import string
import random
#Aquí definimos el siguiente codigo el cual es generar_contraseña
def generar_contraseña():
    while True:
        contraseña = ""
        #Generamos la longitud que va a tener la contraseña
        longitud_contraseña = random.randint(12, 15)
        # Aquí generamos las posibles opciones en el ALFABETO
        ALFABETO = string.ascii_letters + string.digits + "@#%$&?¿¡!*"
        # Aquí generamos la contraseña según la longitud obtenida utilizamos _ dentro del for para decirle al programa que solo nos interesa repetir la acción y no el valor de la variable
        for _ in range(longitud_contraseña):
            contraseña += random.choice(ALFABETO)
        #verificamos requisito de la contraseña, si no se cumple, se reinicia
        if not contraseña[0].isalpha():
            continue  
        #Con esto estamos comprobando si la contraseña tiene menos de 2 digitos vuelva a iniciar el proceso hasta que la longitud de digitos sea superior a 2
        digitos = [c for c in contraseña if c.isdigit()]
        if len(digitos) < 2:
            continue
        #Aquí estamos realizando la misma verificación, solo que en esta opción los caracteres especiales no se pueden repetir por lo que convertimos la variable especiales en un conjunto para que no se repitan y si la longitud es inferior a 2 se repite el proceso
        caracteres_especiales = "@#%$&?¿¡!*"
        especiales = [c for c in contraseña if c in caracteres_especiales]
        if len(especiales) < 2 or len(set(especiales)) <=1:
            continue
        #Aquí comprobamos si al menos contiene dos letras minúsculas y sólo dos letras mayúsculas
        minusculas = [c for c in contraseña if c.islower()]
        mayusculas = [c for c in contraseña if c.isupper()]
        if len(minusculas) < 2 or len(mayusculas) != 2:
            continue
        #Si se cumplen todos los requisitos, la contraseña es válida y se devuelve a la variable contraseña que tenemos en el inicio
        return contraseña

#Aquí estamosañadiendo la función generar_contraseña a la variable contraseña segura y luego decimos al programa que realice un print de la nueva variable que tiene como resultado la contraseña con todas las condiciones cumplidas
contraseña_segura = generar_contraseña()
print("La contraseña segura es:", contraseña_segura)
print(len(contraseña_segura))
