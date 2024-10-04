#Escriba un programa en Python, que pida al usuario un número entero. El número
# será valido si es mayor o igual a 2 y menor o igual a10 o menor o igual a -2 y
# mayor o igual que -10. El programa deberá imprimir según el número leído el
# patrón de figura que se muestra en el cuadro de abajo
valor = int(input("Establece un valor entre 2/10 y -2/-10: "))
if valor >= 2 and valor <= 10:
     print("adios mundo")
elif valor <= -2 and valor >= -10:
    print("hola mundo")
else:
     print("Adios mundo")