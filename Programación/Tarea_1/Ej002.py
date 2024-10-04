# Se desea realizar un programa que permita convertir datos de tiempo expresado
# en días, horas, minutos y segundos a milisegundos y viceversa.
# El programa debe pedir al usuario el tipo de conversión a realizar y debe validar
# todos los datos de entrada. Deben decidir como debe ser la entrada de datos en
# ambos casos y una vez realizados los cálculos correspondientes se debe mostrar
# como respuesta tanto los datos originales y el resultado de la conversión.
modo = input("Pasar a milisegundos (P) o convertir de milisegundos a dias, horas, minutos y segundos (C): ").upper()
if modo == "P":
    tiempo = input("Establece una cantidad de días, horas, minutos y segundos para convertilos en milisegundos, solo se deben insertar números: ").split()
    calculo = (tiempo[0]*86400000) + (tiempo[1] * 3600000) + (tiempo[2] * 60000) + (tiempo[3] * 1000)
    print(f"{calculo} milisegundos.")
elif modo == "C":
    timepo = input("Establece una cantidad de milisegundos para convertirlos: ")
else:
    print("Establece una opción valida")