# Escriba un programa en Python, que pida al usuario un número entero. El número
# será valido si es mayor o igual a 2 y menor o igual a 10 o menor o igual a -2 y
# mayor o igual que -10. El programa deberá imprimir según el número leído el
# patrón de figura que se muestra en el cuadro de abajo

bucle = 1

while bucle == 1:
    choose = int(input("Inserte un número: "))

    if choose >= 2 and choose <= 10:
        print("placeholder")
    
    elif choose <= -2 and choose >= -10:
        print("placeholder")
        
    else:
        print("Inserte una número válido....")