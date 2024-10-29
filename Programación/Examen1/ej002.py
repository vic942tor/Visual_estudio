# Escriba un programa en Python que permita escribir por pantalla el siguiente
# patrón. Se lee como dato un número entero impar que representa el número de
# filas que contiene el patrón. El programa debe verificar que el número leído es
# impar y mayor o igual a 3

#Solicita al usuario un número impar mayor o igual a 3
try:
    n = int(input("Introduce un número impar mayor o igual a 3: "))
    #Verifica que el número es impar y mayor o igual a 3
    if n >= 3 and n % 2 != 0:
    #Establece el patron a dibujar según el número establecido por el usuario
        for i in range(n, 0, -2): 
            for j in range(i, 0, -1):
                print("*", end="")
            print()
    else:
        print("El número debe ser un entero impar y mayor o igual a 3.")
except:
    print("Por favor, introduce un número entero válido.")




