# Escriba un programa en Python, que pida al usuario un número entero. El número
# será valido si es mayor o igual a 2 y menor o igual a 10 o menor o igual a -2 y
# mayor o igual que -10. El programa deberá imprimir según el número leído el
# patrón de figura que se muestra en el cuadro de abajo

respuesta = int(input("Introduce un número: "))
if (2 <= respuesta <= 10) or (-10 <= respuesta <= -2):
    #Con esto utilizaremos el valor absoluto para poder realizar la forma de la figura sin preocuparnos de los signos.
    numero = abs(respuesta)
    if respuesta > 0:
        #Aquí generamos el patron de la figura para los número positivos concadenando los asteriscos en función de i y los espacios según el doble de la diferencia de la variable numero 
        for i in range(numero, 0, -1):
            print("*" * i + " " * (2 * (numero - i)) + "*" * i)
    elif respuesta < 0:
        #Aquí realizamos la misma operación pero teniendo en cuenta que debemos establecerlo de forma invertida
        for i in range(1, numero + 1):
            print("*" * i + " " * (2 * (numero - i)) + "*" * i)
else:
    print("Número incorrecto, por favor establezca un número válido")
