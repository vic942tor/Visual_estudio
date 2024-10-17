#Una palabra se considera creciente se considera que sus letras van en forma creciente
# palabra = input("Escriba una palabra: ").lower()
# anterior = palabra[0]
# for posicion in palabra:
#     if posicion < anterior:
#         print("No es creciente")
#         break
#     anterior = posicion
# else:
#     print("Es creciente")
# Una contraseña se considera segura si cumple las siguientes condiciones, al menos 8 caracteres, 
# una letra mayuscula, una letra minuscula,almenos 1 digito, un caracter especial de @,#,%,[],()!¡
#Escribir un programa que lea una contraseña y diga que es segura
contraseña = input("Escriba una contraseña para verificar la seguridad: ")
ALFABETOM = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
ALFABETOm = "abcdefghijklmnñopqrstuvwxyz"
ESPECIAL = "@#%[]()"
NUMEROS = "0123456789"
Hay_minusculas = False 
Hay_mayuscilas = False 
Hay_digitos = False 
Hay_especiales = False 
if len(contraseña) >= 1 and len(contraseña) > 8:
    for i in contraseña:
        if i in ALFABETOm:
            Hay_minusculas = True
        elif i in ALFABETOM:
            Hay_mayuscilas = True
        elif i in ESPECIAL:
            Hay_especiales = True
        elif i in NUMEROS:
            Hay_digitos = True
else:
      print("La contraseña no es segura")  
        
        
        